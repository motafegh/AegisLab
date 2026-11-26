"""Offline semantics exercise, NOT a Sigma converter or certified backend.

Run from repo root with PYTHONPATH=src python3 examples/sigma_semantics_comparison.py.
Uses trusted local teaching YAML (PyYAML) and independent SQLite queries.
"""
import json
import sqlite3
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml
from aegislab.ssh_incident import analyze

RULE = Path("examples/ssh-failure-correlation.sigma.yml")


def event(second, port, user="labuser", ip="10.10.0.1", outcome="Failed"):
    t = datetime(2026, 11, 22, 10, 0, tzinfo=timezone.utc) + timedelta(seconds=second)
    return {"observed_at": t.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "message": f"sshd[201]: {outcome} publickey for {user} from {ip} port {port} ssh2"}


def compare(report, span, threshold, outcome):
    # Same normalized observations. Dedup key matches Stage B's documented identity.
    # Integer Unix seconds avoid floating-point timestamp boundary artifacts.
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE events (t INTEGER, ip TEXT, username TEXT, port INTEGER, pid INTEGER, source TEXT, outcome TEXT)")
        db.executemany("INSERT INTO events VALUES (?,?,?,?,?,?,?)", [
            (int(datetime.fromisoformat(e["observed_at"].replace("Z","+00:00")).timestamp()),
             e["source_ip"], e["username"], e["source_port"], e["sshd_pid"],
             e["source_id"], e["outcome"]) for e in report["events"]])
        bucket = db.execute("""
            SELECT DISTINCT ip, username FROM (
                SELECT ip, username, t / ? AS bucket, COUNT(*) AS n
                FROM events WHERE outcome = ?
                GROUP BY ip, username, bucket HAVING n >= ?
            ) ORDER BY ip, username
        """, (span, outcome, threshold)).fetchall()
        sliding = db.execute("""
            WITH distinct_events AS (
                SELECT DISTINCT t, ip, username, port, pid, source, outcome
                FROM events WHERE outcome = ?
            )
            SELECT DISTINCT a.ip, a.username FROM distinct_events a
            WHERE (SELECT COUNT(*) FROM distinct_events b
                   WHERE b.ip = a.ip AND b.username = a.username
                   AND b.t BETWEEN a.t - ? AND a.t) >= ?
            ORDER BY a.ip, a.username
        """, (outcome, span, threshold)).fetchall()
    reference = sorted((f["subject"]["source_ip"], f["subject"]["username"])
                       for f in report["findings"])
    return {"reference_subjects": reference, "fixed_bucket_raw_count_subjects": bucket,
            "sliding_distinct_subjects": sliding, "accepted": len(report["events"]),
            "quarantined": report["source"]["quarantined_record_count"],
            "duplicate_failures_ignored": report["source"]["duplicate_failure_observations_ignored"],
            "reference_status": report["status"]}


def main():
    base, correlation = list(yaml.safe_load_all(RULE.read_text()))
    c = correlation["correlation"]
    assert c["type"] == "event_count" and c["rules"] == [base["name"]]
    assert c["group-by"] == ["source_ip", "username"]
    assert c["timespan"] == "120s" and c["condition"] == {"gte": 3}
    assert base["detection"]["condition"] == "selection"
    outcome = base["detection"]["selection"]["outcome"]
    assert outcome == "failed_publickey"
    cases = {
        "ordinary": [event(0,51001),event(30,51002),event(80,51003),event(90,51004,outcome="Accepted")],
        "cross_bucket": [event(110,51001),event(119,51002),event(120,51003)],
        "exact_boundary": [event(0,51001),event(60,51002),event(120,51003)],
        "outside_boundary": [event(0,51001),event(60,51002),event(121,51003)],
        "duplicates": [event(0,51001),event(0,51001),event(40,51002)],
        "different_accounts": [event(0,51001),event(30,51002,user="admin"),event(80,51003)],
        "quarantine_gap": [event(0,51001),"invalid-json",event(30,51002),event(80,51003)],
    }
    result = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, items in cases.items():
            path = Path(tmp) / (name + ".jsonl")
            path.write_text("".join((json.dumps(i) if isinstance(i,dict) else i)+"\n" for i in items))
            report = analyze(path, source_id="fixture:sigma:"+name, source_kind="synthetic")
            result[name] = compare(report, int(c["timespan"][:-1]), c["condition"]["gte"], outcome)
            assert result[name]["reference_subjects"] == result[name]["sliding_distinct_subjects"]
    assert result["cross_bucket"]["reference_subjects"] and not result["cross_bucket"]["fixed_bucket_raw_count_subjects"]
    assert result["exact_boundary"]["reference_subjects"] and not result["exact_boundary"]["fixed_bucket_raw_count_subjects"]
    assert not result["duplicates"]["reference_subjects"] and result["duplicates"]["fixed_bucket_raw_count_subjects"]
    print(json.dumps({"method":"handwritten_sql_not_sigma_conversion","cases":result},indent=2))


if __name__ == "__main__":
    main()
