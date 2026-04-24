# HexaCore

HexaCore is a modular cybersecurity framework built for educational purposes and authorized penetration testing.
It combines multiple security tools into one scalable platform with a Python-based GUI and a Bash execution core.

---

## Features

* Recon (WHOIS, Nmap, DNS, Subdomain)
* Bruteforce (Hydra, John the Ripper)
* Network tools (MAC changer, IP tools, WiFi scan)
* OSINT (username & email generation, info lookup)
* Exploit research (Searchsploit integration)

---

## Architecture

* GUI (Python / CustomTkinter)
* Modules (API layer)
* Core (Router, Executor, Logger)
* Bash Core (tool execution)

---

## Installation

```bash
git clone https://github.com/your-username/hexacore.git
cd hexacore
pip install -r requirements.txt
python main.py
```

---

## Usage

Run the main interface:

```bash
python main.py
```

---

## Disclaimer

This tool is created for educational purposes and authorized security testing only.
Do not use it on systems without permission.

---

## License

MIT License
