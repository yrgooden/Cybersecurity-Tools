# 🔐 Cybersecurity Tools

A collection of cybersecurity tools built in Python and HTML/JavaScript, demonstrating core security concepts including network scanning, password analysis, and encrypted breach detection.

---

## Projects

### 1. Port Scanner (`port_scanner.py`)

A multithreaded network port scanner built in Python that mimics core functionality of professional tools like nmap.

**Features**
- Resolves hostnames to IP addresses
- Scans a configurable port range using concurrent threads for speed
- Banner grabbing to fingerprint running services
- Clean CLI output with port, status, and service info
- Command-line arguments via `argparse`

**Usage**
```bash
# Default scan (ports 1-1024 on scanme.nmap.org)
python port_scanner.py

# Custom target and port range
python port_scanner.py scanme.nmap.org -s 1 -e 1024

# Scan specific range
python port_scanner.py 192.168.1.1 -s 20 -e 100
```

**Example Output**
```
--------------------------------------------------
  Target   : scanme.nmap.org
  IP       : 45.33.32.156
  Ports    : 1 - 1024
  Started  : 2026-04-05 10:06:14
--------------------------------------------------
PORT     STATUS     BANNER
--------------------------------------------------
22       OPEN       SSH-2.0-OpenSSH_6.6.1p1 Ubuntu
80       OPEN       HTTP/1.1 200 OK
--------------------------------------------------
  Scan complete. 2 open port(s) found.
--------------------------------------------------
```

**Skills Demonstrated**
- Python socket programming and networking fundamentals
- Multithreading for performance optimization
- Service fingerprinting via banner grabbing
- CLI tool design with argparse

**Requirements**
- Python 3.x
- No external libraries — uses only built-in `socket`, `threading`, and `argparse`

> ⚠️ Only scan hosts you own or have explicit permission to scan. `scanme.nmap.org` is provided by the nmap project for legal practice scanning.

---

### 2. Password Strength Checker (`password_checker.html`)

A browser-based password analysis tool that evaluates password strength in real time using industry-standard security metrics.

**Features**
- Live strength meter (Critical → Weak → Moderate → Strong → Fortress)
- Rule checklist: length, uppercase, lowercase, numbers, symbols, 16+ chars
- Entropy calculation in bits (standard cryptographic metric)
- Crack time estimate based on offline GPU brute-force rate (10B guesses/sec)
- Common password detection against known attack wordlists
- Have I Been Pwned (HIBP) API integration using k-anonymity — your password never leaves your machine
- Strong password generator (20 characters, mixed character sets)

**Usage**

Open `password_checker.html` directly in any browser — no server or install required.

Or visit the live demo: https://yrgooden.github.io/Cybersecurity-Tools/password_checker.html

**Skills Demonstrated**
- Vanilla JavaScript and Web Crypto API (SHA-1 hashing)
- REST API integration with privacy-preserving k-anonymity model
- Entropy and crack time calculations used in real security tooling
- Responsive UI built with HTML/CSS

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/yrgooden/cybersecurity-tools.git
cd cybersecurity-tools

# Run the port scanner
python port_scanner.py

# Open the password checker
open password_checker.html   # macOS
start password_checker.html  # Windows
```

---

## Roadmap

- [ ] Export port scan results to JSON/CSV
- [ ] Add service name lookup to port scanner
- [ ] Add crack time breakdown by attack type
- [ ] Dark/light mode toggle for password checker

---

## Disclaimer

These tools are built for educational purposes and personal learning. Always ensure you have proper authorization before scanning any network or system you do not own.

---

## Yulonda Gooden

Built as part of a cybersecurity portfolio. Focused on Python scripting, network security, and browser-based security tooling.
