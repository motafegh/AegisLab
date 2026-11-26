"""Deadline supervision checks; HTTP test server is ephemeral loopback only."""
import json
import subprocess
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch

from aegislab.inference_deadline import infer_bounded
from aegislab.local_inference import LocalConfig, infer
from aegislab.investigator_context import prepare_context
from test_local_investigator import report, envelope, candidate


class DeadlineTests(unittest.TestCase):
    def setUp(self):
        self.context = prepare_context(report())["context"]

    def test_deadline_config(self):
        for x in (0, -1, 121, float("nan"), True):
            with self.assertRaises(ValueError):
                LocalConfig(deadline=x)

    def test_worker_launch_error(self):
        with patch("aegislab.inference_deadline.subprocess.run", side_effect=OSError):
            r = infer_bounded(self.context, LocalConfig())
        self.assertEqual(r["reason"], "worker_launch_failed")

    def test_worker_invalid_result(self):
        with patch("aegislab.inference_deadline.subprocess.run",
                   return_value=subprocess.CompletedProcess([], 0, b"not json")):
            r = infer_bounded(self.context, LocalConfig())
        self.assertEqual(r["reason"], "invalid_worker_result")

    def test_worker_nonzero_exit(self):
        with patch("aegislab.inference_deadline.subprocess.run",
                   return_value=subprocess.CompletedProcess([], 2, b"")):
            r = infer_bounded(self.context, LocalConfig())
        self.assertEqual(r["reason"], "worker_failed")

    def test_timeout_preserves_baseline(self):
        from aegislab.investigator import investigate
        import importlib.util
        if importlib.util.find_spec("jsonschema") is None:
            self.skipTest("optional jsonschema unavailable")
        baseline = report()
        with patch("aegislab.inference_deadline.subprocess.run",
                   side_effect=subprocess.TimeoutExpired(["worker"], 0.75)):
            r = investigate(baseline, LocalConfig(deadline=0.75))
        self.assertEqual(r["baseline"], baseline)
        self.assertEqual(r["investigation"]["status"], "not_admitted")
        self.assertEqual(r["investigation"]["reason"], "deadline_exceeded")

    def test_actual_loopback_slow_response(self):
        body = json.dumps(envelope(json.dumps(candidate(self.context)))).encode()
        seen = threading.Event()

        class SlowHandler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                self.rfile.read(int(self.headers["Content-Length"]))
                seen.set()
                self.send_response(200)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                try:
                    # Each I/O gap is shorter than the socket timeout.
                    for pos in range(0, len(body), 32):
                        self.wfile.write(body[pos:pos + 32])
                        self.wfile.flush()
                        time.sleep(0.08)
                except (BrokenPipeError, ConnectionResetError):
                    pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), SlowHandler)
        thread = threading.Thread(target=server.serve_forever,
                                  kwargs={"poll_interval": 0.02}, daemon=True)
        thread.start()
        try:
            config = LocalConfig(port=server.server_port, timeout=2, deadline=0.75)
            low_level = infer(self.context, config)
            self.assertEqual(low_level["status"], "completed_unvalidated")
            self.assertGreater(low_level["elapsed_seconds"], config.deadline)
            seen.clear()
            bounded = infer_bounded(self.context, config)
            self.assertTrue(seen.is_set())
            self.assertEqual(bounded["reason"], "deadline_exceeded")
            self.assertNotIn("content", bounded)
            self.assertLess(bounded["elapsed_seconds"], 4)
            print("Controlled loopback slow-response: direct",
                  low_level["elapsed_seconds"], "s; supervised",
                  bounded["elapsed_seconds"], "s")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

if __name__ == "__main__":
    unittest.main()
