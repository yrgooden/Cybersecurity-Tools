import socket
import threading
import argparse
from datetime import datetime

# ─── Configuration ───────────────────────────────────────────
TIMEOUT = 0.5                # Seconds to wait per port
THREADS = 100                # Concurrent threads

# ─── Globals ─────────────────────────────────────────────────
open_ports = []
lock = threading.Lock()

# ─── Banner Grabbing ─────────────────────────────────────────
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(TIMEOUT)
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner.split("\n")[0] if banner else None
    except:
        return None

# ─── Port Scan ───────────────────────────────────────────────
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            banner = grab_banner(ip, port)
            with lock:
                open_ports.append((port, banner))
    except socket.error:
        pass

# ─── Main ────────────────────────────────────────────────────
def run_scan(target, port_range):
    print("-" * 50)
    print(f"  Target   : {target}")

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"  Error: Could not resolve hostname '{target}'")
        return

    print(f"  IP       : {ip}")
    print(f"  Ports    : {port_range[0]} - {port_range[1]}")
    print(f"  Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    threads = []
    for port in range(port_range[0], port_range[1] + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

        # Throttle: keep max THREADS running at once
        if len(threads) >= THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    # ─── Results ─────────────────────────────────────────────
    print(f"\n{'PORT':<8} {'STATUS':<10} BANNER")
    print("-" * 50)
    if open_ports:
        for port, banner in sorted(open_ports):
            banner_str = banner if banner else "N/A"
            print(f"{port:<8} {'OPEN':<10} {banner_str[:60]}")
    else:
        print("  No open ports found.")

    print("-" * 50)
    print(f"  Scan complete. {len(open_ports)} open port(s) found.")
    print("-" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple Python Port Scanner",
        epilog="Example: python port_scanner.py scanme.nmap.org -s 1 -e 1024"
    )
    parser.add_argument("target", nargs="?", default="scanme.nmap.org",
                        help="Hostname or IP to scan (default: scanme.nmap.org)")
    parser.add_argument("-s", "--start", type=int, default=1,
                        help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024,
                        help="End port (default: 1024)")

    args = parser.parse_args()
    run_scan(target=args.target, port_range=(args.start, args.end))
