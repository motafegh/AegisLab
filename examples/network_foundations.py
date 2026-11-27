"""R2.2 safe networking exercise: own loopback sockets; route lookups send no packets.
No sudo, external connection, raw host addresses in retained output or config changes.
"""
import ipaddress
import json
import socket
import subprocess


def run(args):
    p = subprocess.run(args, capture_output=True, text=True, timeout=5)
    return {"exit_code": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip()}


def route(destination):
    r = run(["ip", "-j", "-4", "route", "get", destination])
    if r["exit_code"]:
        return {"exit_code": r["exit_code"]}
    # Preserve relevant topology facts without publishing actual host/gateway addresses.
    a = json.loads(r["stdout"])[0]
    return {"destination": destination, "interface": a.get("dev"),
            "gateway_present": bool(a.get("gateway")),
            "source_is_loopback": ipaddress.ip_address(a["prefsrc"]).is_loopback if a.get("prefsrc") else None,
            "table": a.get("table"), "type": a.get("type")}


def main():
    r = {"route_loopback": route("127.0.0.1"), "route_documentation_address": route("192.0.2.20"),
         "subnet_exercise": {"network": "10.20.0.0/24",
                             "same_subnet": ipaddress.ip_address("10.20.0.20") in ipaddress.ip_network("10.20.0.0/24"),
                             "different_subnet": ipaddress.ip_address("10.20.1.20") not in ipaddress.ip_network("10.20.0.0/24")}}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        port = server.getsockname()[1]
        # Socket owns a local address but is not listening yet.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.settimeout(2)
            try:
                c.connect(("127.0.0.1", port))
            except OSError as e:
                r["tcp_before_listen"] = {"error": type(e).__name__, "errno": e.errno}
            else:
                r["tcp_before_listen"] = {"unexpected": "connected"}
        server.listen(1)
        server.settimeout(2)
        r["tcp_listen"] = run(["ss", "-ltn", "sport", "=", f":{port}"])
        # Capture permission only for this own, idle listener. No traffic generated
        # while attempting capture; bounded timeout even if permission is granted.
        iface = r["route_loopback"].get("interface")
        if iface:
            p = subprocess.run(["timeout", "2", "tcpdump", "-p", "-i", iface, "-nn",
                                "-c", "1", "tcp", "and", "port", str(port)],
                               capture_output=True, text=True, timeout=4)
            r["capture_probe"] = {"exit_code": p.returncode,
                                  "permission_denied": "permission" in p.stderr.lower() or "permitted" in p.stderr.lower(),
                                  "packets_retained": 0}
        with socket.create_connection(("127.0.0.1", port), timeout=2) as c:
            conn, addr = server.accept()
            with conn:
                conn.settimeout(2)
                r["tcp_endpoints"] = run(["ss", "-tn", "(", "sport", "=", f":{port}",
                                           "or", "dport", "=", f":{port}", ")"])
                c.sendall(b"hello")
                received = bytearray()
                while len(received) < 5:
                    chunk = conn.recv(5 - len(received))
                    if not chunk:
                        raise RuntimeError("unexpected TCP end of stream")
                    received.extend(chunk)
                r["tcp_payload"] = received.decode()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver, socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        receiver.bind(("127.0.0.1", 0))
        receiver.settimeout(2)
        port = receiver.getsockname()[1]
        r["udp_bound"] = run(["ss", "-lun", "sport", "=", f":{port}"])
        sender.sendto(b"one", receiver.getsockname())
        sender.sendto(b"two", receiver.getsockname())
        r["udp_datagrams"] = [receiver.recvfrom(32)[0].decode() for _ in range(2)]
    assert r["tcp_before_listen"].get("error") == "ConnectionRefusedError"
    assert r["tcp_payload"] == "hello" and r["udp_datagrams"] == ["one","two"]
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
