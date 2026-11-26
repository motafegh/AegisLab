"""Supervise the optional local inference client in a disposable subprocess.

The deadline bounds the caller's wait for the worker, not server-side GPU work.
Process creation, scheduling and termination/reaping can add overhead.
Only a fixed internal Python module is launched; no shell or model commands.
"""
from __future__ import annotations

from dataclasses import asdict
import json
import subprocess
import sys
import time
from typing import Any

from .local_inference import LocalConfig, infer, request_body, MAX_REQUEST_BYTES, MAX_RESPONSE_BYTES, PROMPT_VERSION
from .investigator_contract import strict_json

MAX_WORKER_INPUT = MAX_REQUEST_BYTES
MAX_WORKER_OUTPUT = MAX_RESPONSE_BYTES * 6 + 8192


def infer_bounded(context: dict[str, Any], config: LocalConfig) -> dict[str, Any]:
    start = time.monotonic()
    result = {"status": "not_completed", "reason": None,
              "model_requested": config.model, "prompt_version": PROMPT_VERSION,
              "max_tokens": config.max_tokens, "socket_timeout_seconds": config.timeout,
              "deadline_seconds": config.deadline}

    def finish(reason: str) -> dict[str, Any]:
        result.update(reason=reason, elapsed_seconds=round(time.monotonic() - start, 3))
        return result

    try:
        request_body(context, config)  # reject invalid/oversized input before spawning
        payload = json.dumps({"context": context, "config": asdict(config)},
                             separators=(",", ":"), allow_nan=False).encode("utf-8")
        if len(payload) > MAX_WORKER_INPUT:
            return finish("worker_input_budget_exceeded")
    except (ValueError, TypeError, KeyError, RecursionError):
        return finish("invalid_or_oversized_request")
    remaining = config.deadline - (time.monotonic() - start)
    if remaining <= 0:
        return finish("deadline_exceeded")
    try:
        completed = subprocess.run(
            [sys.executable, "-m", "aegislab.inference_deadline", "--worker"],
            input=payload, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=remaining, check=False,
        )
    except subprocess.TimeoutExpired:
        # subprocess.run kills and waits for its child on timeout.
        return finish("deadline_exceeded")
    except OSError:
        return finish("worker_launch_failed")
    if time.monotonic() - start >= config.deadline:
        return finish("deadline_exceeded")
    if completed.returncode != 0 or len(completed.stdout) > MAX_WORKER_OUTPUT:
        return finish("worker_failed")
    try:
        observed = strict_json(completed.stdout.decode("utf-8"))
        if not isinstance(observed, dict):
            raise ValueError("invalid worker result")
        if observed.get("status") not in {"not_completed", "completed_unvalidated"}:
            raise ValueError("invalid worker status")
        if observed["status"] == "completed_unvalidated":
            if observed.get("reason") is not None or not isinstance(observed.get("content"), str):
                raise ValueError("invalid completed result")
        elif not isinstance(observed.get("reason"), str):
            raise ValueError("missing failure reason")
        if observed.get("model_requested") != config.model:
            raise ValueError("unexpected worker configuration")
    except (ValueError, TypeError, RecursionError):
        return finish("invalid_worker_result")
    observed["worker_elapsed_seconds"] = observed.get("elapsed_seconds")
    observed["elapsed_seconds"] = round(time.monotonic() - start, 3)
    observed["deadline_seconds"] = config.deadline
    return observed


def _worker() -> int:
    raw = sys.stdin.buffer.read(MAX_WORKER_INPUT + 1)
    if len(raw) > MAX_WORKER_INPUT:
        return 2
    try:
        data = strict_json(raw.decode("utf-8"))
        config = LocalConfig(**data["config"])
        result = infer(data["context"], config)
        output = json.dumps(result, separators=(",", ":"), allow_nan=False).encode("utf-8")
        if len(output) > MAX_WORKER_OUTPUT:
            return 2
        sys.stdout.buffer.write(output)
    except (ValueError, TypeError, KeyError, RecursionError):
        return 2
    return 0


if __name__ == "__main__":
    if sys.argv[1:] != ["--worker"]:
        raise SystemExit(2)
    raise SystemExit(_worker())
