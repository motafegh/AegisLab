"""R1 native Sigma conversion and offline execution. Trusted repository rules only.
Run with isolated Sigma environment: PYTHONPATH=src <venv>/bin/python examples/sigma_native_comparison.py
No live collection, external platform or model calls. Synthetic data only.
"""
import importlib.metadata as metadata
import json
import sqlite3
import tempfile
from pathlib import Path

import yaml
from sigma.collection import SigmaCollection
from sigma.backends.sqlite import sqliteBackend
from aegislab.ssh_incident import analyze
from sigma_semantics_comparison import event

RULE = Path("examples/ssh-failure-correlation.sigma.yml")
IDENTITY = ("username", "source_ip", "observed_at", "source_port",
            "outcome", "source_id", "sshd_pid")


def queries():
    # Native converter, not handwritten translation. Map timestamp and stable
    # record-derived event identity explicitly rather than use backend defaults.
    backend = sqliteBackend(table="logs", timestamp_field="observed_at",
                            event_id_field="event_id")
    base = list(yaml.safe_load_all(RULE.read_text()))[0]
    single = backend.convert(SigmaCollection.from_yaml(yaml.safe_dump(base)))[0]
    correlation = sqliteBackend(table="logs", timestamp_field="observed_at",
                                 event_id_field="event_id").convert(
        SigmaCollection.from_yaml(RULE.read_text()))[0]
    return single, correlation


def deduplicate(events):
    seen = set()
    for e in events:
        key = tuple(e[k] for k in IDENTITY)
        if e["outcome"] == "failed_publickey":
            if key in seen:
                continue
            seen.add(key)
        yield e


def execute(events, base_query, correlation_query):
    with sqlite3.connect(":memory:") as db:
        db.row_factory = sqlite3.Row
        db.execute("CREATE TABLE logs (event_id TEXT PRIMARY KEY, observed_at TEXT, outcome TEXT, source_ip TEXT, username TEXT)")
        db.executemany("INSERT INTO logs VALUES (?,?,?,?,?)", [
            tuple(e[k] for k in ("event_id","observed_at","outcome","source_ip","username"))
            for e in events])
        db.execute("PRAGMA query_only=ON")
        base = [dict(r) for r in db.execute(base_query)]
        alerts = [dict(r) for r in db.execute(correlation_query)]
    for a in alerts:
        a["group_keys"] = json.loads(a["group_keys"])
        a["event_ids"] = json.loads(a["event_ids"])
        a["child_alert_ids"] = json.loads(a["child_alert_ids"])
        assert all(ref.startswith("0:") and ref[2:] in {e["event_id"] for e in events}
                   for ref in a["event_ids"])
    return {"base_matches": len(base), "alerts": alerts,
            "subjects": sorted({(a["group_keys"]["source_ip"], a["group_keys"]["username"])
                                for a in alerts})}


def main():
    base, correlation = queries()
    cases = {
        "ordinary": [event(0,51001),event(30,51002),event(80,51003),event(90,51004,outcome="Accepted")],
        "cross_bucket": [event(110,51001),event(119,51002),event(120,51003)],
        "exact_boundary": [event(0,51001),event(60,51002),event(120,51003)],
        "outside_boundary": [event(0,51001),event(60,51002),event(121,51003)],
        "duplicates": [event(0,51001),event(0,51001),event(40,51002)],
        "different_accounts": [event(0,51001),event(30,51002,user="admin"),event(80,51003)],
        "quarantine_gap": [event(0,51001),"invalid-json",event(30,51002),event(80,51003)],
        "case_sensitive_accounts": [event(0,51001,user="Labuser"),event(30,51002),event(80,51003)],
        "four_failures": [event(0,51001),event(20,51002),event(40,51003),event(60,51004)],
        "normal": [event(0,51001,outcome="Accepted"),event(30,51002)],
    }
    results = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, items in cases.items():
            path = Path(tmp) / (name + ".jsonl")
            path.write_text("".join((json.dumps(i) if isinstance(i,dict) else i)+"\n" for i in items))
            report = analyze(path, source_id="fixture:sigma-native:"+name, source_kind="synthetic")
            events = report["events"]
            results[name] = {"reference_status": report["status"],
                             "reference_findings": report["findings"],
                             "reference_subjects": sorted((f["subject"]["source_ip"], f["subject"]["username"]) for f in report["findings"]),
                             "accepted_event_ids": [e["event_id"] for e in events],
                             "quarantined": report["source"]["quarantined_record_count"],
                             "native_raw": execute(events, base, correlation),
                             "native_reference_dedup": execute(list(deduplicate(events)), base, correlation)}
    # Explicit expected contrast cases, not a claim of universal equivalence.
    assert results["ordinary"]["native_raw"]["subjects"] == results["ordinary"]["reference_subjects"]
    assert results["exact_boundary"]["native_raw"]["subjects"]
    assert not results["outside_boundary"]["native_raw"]["subjects"]
    assert results["duplicates"]["native_raw"]["subjects"] and not results["duplicates"]["native_reference_dedup"]["subjects"]
    assert not results["case_sensitive_accounts"]["reference_subjects"] and results["case_sensitive_accounts"]["native_reference_dedup"]["subjects"]
    assert len(results["four_failures"]["native_raw"]["alerts"]) > len(results["four_failures"]["reference_findings"])
    print(json.dumps({"versions": {n:metadata.version(n) for n in ("sigma-cli","pysigma","pysigma-backend-sqlite")},
                      "sqlite":sqlite3.sqlite_version,"mapping":{"table":"logs","timestamp_field":"observed_at","event_id_field":"event_id"},
                      "base_query":base,"correlation_query":correlation,"cases":results},indent=2))

if __name__ == "__main__":
    main()
