"""R2/F1: disposable Linux process, file permissions, and TCP socket observations.

Run from repository root: python3 examples/linux_process_foundations.py
Only own files/processes and a kernel-assigned IPv4 loopback port; no sudo.
No real SSH logs, persistent configuration, or external connections.
"""
import json
import os
from pathlib import Path
import selectors
import socket
import stat
import subprocess
import sys
import tempfile

CHILD = """
import json, os, socket, sys
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    server.settimeout(5)
    print(json.dumps({"pid": os.getpid(), "ppid": os.getppid(),
                      "port": server.getsockname()[1], "listener_fd": server.fileno()}),
          flush=True)
    with server.accept()[0] as connection:
        connection.settimeout(5)
        print(json.dumps({"accepted_fd": connection.fileno()}), flush=True)
        assert connection.recv(1) == b"x"
        connection.sendall(b"y")
        print("completed controlled exchange", file=sys.stderr, flush=True)
"""

def observe(args):
    r = subprocess.run(args, capture_output=True, text=True, timeout=4, check=False)
    return {"command": args, "exit_code": r.returncode,
            "stdout": r.stdout.strip(), "stderr": r.stderr.strip()}

def line(p):
    with selectors.DefaultSelector() as sel:
        sel.register(p.stdout, selectors.EVENT_READ)
        if not sel.select(timeout=5):
            raise TimeoutError("child readiness timed out")
    data = p.stdout.readline()
    if not data:
        raise RuntimeError("child exited before readiness")
    return json.loads(data)

def fd_links(pid, fds):
    out = {}
    for fd in fds:
        try:
            out[str(fd)] = os.readlink(f"/proc/{pid}/fd/{fd}")
        except OSError as exc:
            out[str(fd)] = type(exc).__name__
    return out

def main():
    if os.geteuid() == 0:
        raise SystemExit("Run as an ordinary user, not root")
    result = {}
    with tempfile.TemporaryDirectory(prefix="aegislab-r2-f1-") as temp:
        file = Path(temp) / "observation.txt"
        file.write_text("disposable teaching data\n")
        file.chmod(0o600)
        result["file"] = {"mode": oct(stat.S_IMODE(file.stat().st_mode)),
                          "owned_by_effective_user": file.stat().st_uid == os.geteuid(),
                          "read_at_0600": file.read_text().strip()}
        try:
            file.chmod(0)
            try:
                file.read_text()
            except PermissionError:
                result["file"]["read_at_0000"] = "PermissionError"
            else:
                result["file"]["read_at_0000"] = "succeeded_unexpectedly"
        finally:
            file.chmod(0o600)
        result["file"]["mode_restored"] = oct(stat.S_IMODE(file.stat().st_mode))
        child = subprocess.Popen([sys.executable, "-u", "-c", CHILD],
                                 stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
        try:
            ready = line(child)
            assert ready["pid"] == child.pid and ready["ppid"] == os.getpid()
            port = ready["port"]
            result["ready"] = ready
            result["process"] = observe(["ps", "-p", str(child.pid),
                                         "-o", "pid,ppid,stat,comm"])
            result["listener"] = observe(["ss", "-ltnp", "sport", "=", f":{port}"])
            result["fds_listening"] = fd_links(child.pid, [0,1,2,ready["listener_fd"]])
            with socket.create_connection(("127.0.0.1", port), timeout=3) as conn:
                accepted = line(child)
                result["accepted"] = accepted
                result["connection"] = {"client_port": conn.getsockname()[1],
                                        "server_port": port,
                                        "ss": observe(["ss", "-tnp", "(", "sport", "=", f":{port}",
                                                       "or", "dport", "=", f":{port}", ")"])}
                result["fds_connected"] = fd_links(child.pid, [ready["listener_fd"],accepted["accepted_fd"]])
                conn.sendall(b"x")
                result["application_reply"] = conn.recv(1).decode("ascii")
            stdout, stderr = child.communicate(timeout=5)
            result["child_exit"] = {"returncode": child.returncode, "remaining_stdout": stdout.strip(),
                                    "stderr": stderr.strip()}
            result["process_after_exit"] = observe(["ps", "-p", str(child.pid), "-o", "pid,ppid,stat,comm"])
            result["listener_after_exit"] = observe(["ss", "-ltnp", "sport", "=", f":{port}"])
        finally:
            if child.poll() is None:
                child.kill()
                child.communicate(timeout=3)
    result["temporary_directory_removed"] = not Path(temp).exists()
    result["journal_tag_query"] = observe(["journalctl", "--no-pager", "-n", "2", "-t", "aegislab-r2-f1-no-emitter"])
    assert result["application_reply"] == "y" and result["child_exit"]["returncode"] == 0
    assert result["temporary_directory_removed"]
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
