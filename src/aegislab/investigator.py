"""Provisional opt-in experiment joining context, local inference and validation."""
from __future__ import annotations

from typing import Any

from .investigator_context import prepare_context
from .investigator_contract import ContractError, validate_output, OUTPUT_VERSION
from .local_inference import LocalConfig
from .inference_deadline import infer_bounded


def investigate(report: dict[str, Any], config: LocalConfig, *,
                finding_id: str | None = None, inference=infer_bounded) -> dict[str, Any]:
    """Preserve baseline; never promote generated text to established findings."""
    preparation = prepare_context(report, finding_id=finding_id)
    result = {"baseline": report, "preparation": preparation,
              "investigation": {"status": "not_invoked", "reason": preparation["reason"],
                                "output_version": OUTPUT_VERSION}}
    if not preparation["eligible"]:
        return result
    context = preparation["context"]
    if context["source"]["declared_kind"] != "synthetic":
        result["investigation"]["reason"] = "synthetic_only_experiment"
        return result
    try:
        import jsonschema  # optional for AI; never required for baseline
    except ImportError:
        result["investigation"]["reason"] = "validator_unavailable"
        return result
    transport = inference(context, config)
    result["transport"] = {k: v for k, v in transport.items() if k != "content"}
    if transport["status"] != "completed_unvalidated":
        result["investigation"].update(status="not_admitted", reason=transport["reason"])
        return result
    try:
        result["investigation"] = validate_output(transport["content"], context)
    except ContractError as exc:
        result["investigation"].update(status="not_admitted", reason=str(exc))
    return result
