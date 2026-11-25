"""Provisional C3/C5 output contract. Mechanical validity is not truth."""
from __future__ import annotations

import json
from typing import Any

OUTPUT_VERSION = "aegislab.ssh-investigation.v0.2"
MAX_OUTPUT_BYTES = 16_384
TEXT = {"type": "string", "minLength": 1, "maxLength": 600, "pattern": r"\S"}
IDS = {"type": "array", "items": {"type": "string", "pattern": "^evt-[0-9a-f]{20}$"},
       "minItems": 1, "maxItems": 32, "uniqueItems": True}


def obj(fields):
    return {"type": "object", "properties": fields, "required": list(fields),
            "additionalProperties": False}


OUTPUT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    **obj({
        "hypotheses": {"type": "array", "maxItems": 2, "items": obj({
            "explanation": TEXT, "basis_event_ids": IDS, "limitation": TEXT})},
        "next_check": {"anyOf": [obj({
            "objective": TEXT, "basis_event_ids": IDS, "required_evidence": TEXT,
            "if_present": TEXT, "if_unavailable": TEXT}), {"type": "null"}]},
        "uncertainty": TEXT,
    }),
}
# Server-side structured-output compatibility is provider dependent.
GENERATION_SCHEMA = {k: v for k, v in OUTPUT_SCHEMA.items() if k != "$schema"}


class ContractError(ValueError):
    """An output was not mechanically admitted."""


def unique_pairs(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ContractError("duplicate_json_key")
        out[k] = v
    return out


def reject_constant(value):
    raise ContractError("nonstandard_json_constant")


def strict_json(text):
    return json.loads(text, object_pairs_hook=unique_pairs,
                      parse_constant=reject_constant)


def validate_output(content: str, context: dict[str, Any]) -> dict[str, Any]:
    """Validate shape using optional local jsonschema; then verify event membership."""
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:
        raise ContractError("validator_unavailable") from exc
    if not isinstance(content, str) or len(content.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise ContractError("output_byte_or_type_limit")
    try:
        value = strict_json(content)
    except (ValueError, RecursionError) as exc:
        raise ContractError("invalid_output_json") from exc
    if not Draft202012Validator(OUTPUT_SCHEMA).is_valid(value):
        raise ContractError("output_schema_mismatch")
    events = {e["event_id"]: e for e in context["events"]}
    items = list(value["hypotheses"])
    if value["next_check"] is not None:
        items.append(value["next_check"])
    for item in items:
        if not set(item["basis_event_ids"]) <= events.keys():
            raise ContractError("unknown_or_out_of_context_event_id")
    scope = None
    if value["next_check"] is not None:
        refs = value["next_check"]["basis_event_ids"]
        selected = [events[x] for x in refs]
        scope = {"event_ids": refs,
                 "usernames": sorted({e["username"] for e in selected}),
                 "source_ips": sorted({e["source_ip"] for e in selected}),
                 "observed_at_min": min(e["observed_at"] for e in selected),
                 "observed_at_max": max(e["observed_at"] for e in selected),
                 "target_hostname": None, "coverage": "not_established"}
    return {"status": "admitted_unadjudicated", "output_version": OUTPUT_VERSION,
            "output": value, "derived_scope": scope}
