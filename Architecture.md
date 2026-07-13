<img width="844" height="1864" alt="architecture" src="https://github.com/user-attachments/assets/a171c7d9-05d0-4b52-af5e-e09a8692c440" /># Network Traffic Analysis and Threat Detection using Zeek

## Lab Architecture

This project simulates a Security Operations Center (SOC) environment for monitoring, analyzing, and detecting malicious network activities using Zeek, Wireshark, tcpdump, and Python.

---

## Lab Environment

| Machine | Operating System | Role |
|----------|------------------|------|
| Kali Linux | Kali Linux | Attacker |
| Ubuntu | Ubuntu | Monitoring Server (Zeek Sensor) |
| Windows 11 | Windows 11 | Target Machine |

---

## Network Configuration

- Virtualization Platform: VMware
- Network Mode: Host-Only Network
- All virtual machines communicate within an isolated lab environment.

---

## Monitoring Components

- Zeek Network Security Monitor
- Wireshark
- tcpdump
- Python Detection Scripts

---

## Attack Simulations

### 1. SSH Brute Force Attack
- Tool: Hydra
- Target: Ubuntu SSH Server
- Detection: Zeek `conn.log`, `ssh.log`, Python Detection Script

### 2. TCP SYN Port Scan
- Tool: Nmap
- Target: Ubuntu
- Detection: Zeek `conn.log`, Python Detection Script

### 3. DNS Anomaly Detection
- Tool: nslookup
- Detection: Zeek `dns.log`, Python Detection Script

---

## Detection Workflow

```
Attacker (Kali Linux)
        │
        ▼
Attack Simulation
        │
        ▼
Network Traffic
        │
        ▼
tcpdump (Packet Capture)
        │
        ▼
Zeek Log Generation
(conn.log, ssh.log, dns.log)
        │
        ▼
Python Detection Scripts
        │
        ▼
SOC Investigation
        │
        ▼
Incident Report
```

---

## Project Outcome

- Simulated real-world cyber attacks.
- Captured network traffic using tcpdump.
- Analyzed packets using Wireshark.
- Generated Zeek logs for investigation.
- Developed Python-based detection scripts for automated threat detection.
- Documented findings through incident reports.
<img width="844" height="1864" alt="architecture" src="https://github.com/user-attachments/assets/aa4a1ef1-4a4b-4a13-80bb-4cc70e0120a3" />


