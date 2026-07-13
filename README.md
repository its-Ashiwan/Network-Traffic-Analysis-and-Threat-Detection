

# 📖 Project Overview

This project demonstrates how a Security Operations Center (SOC) analyst investigates network attacks using Zeek, Wireshark, tcpdump, and Python. A virtual lab was built to simulate attacks, capture network traffic, analyze logs, and automate threat detection through custom detection scripts.

---

# 🎯 Objectives

- Simulate real-world cyber attacks in a controlled environment.
- Capture and analyze network traffic.
- Investigate Zeek logs for malicious activities.
- Build custom Python-based threat detection scripts.
- Perform SOC-style incident investigation and reporting.

---

# 🏗️ Lab Architecture

<p align="center">
<img src="Images/architecture.png" width="850">
</p>

---

# 💻 Lab Environment

| Machine | Role |
|----------|------|
| Kali Linux | Attacker |
| Ubuntu | Zeek Monitoring Server |
| Windows 11 | Target Machine |

**Network Mode:** Host-Only Network

---

# 🛠️ Tools & Technologies

- Zeek
- Wireshark
- tcpdump
- Python
- Hydra
- Nmap
- VMware Workstation
- Ubuntu
- Kali Linux
- Windows 11

---

# 📂 Project Structure

```text
zeek-threat-detection-lab/
│
├── Analysis/
├── Detection-Scripts/
├── Images/
├── Incident-Reports/
├── Logs/
├── PCAP/
├── Screenshots/
├── Zeek-Logs/
├── Architecture.md
├── README.md
└── LICENSE
```

---

# 🔄 Detection Workflow

<p align="center">
<img width="1715" height="875" alt="detection_reporting_and_project_structure png" src="https://github.com/user-attachments/assets/4091778d-1724-4f2d-9407-8b2e923918a2" />

</p>

```
Attack Simulation
        │
        ▼
Packet Capture (tcpdump)
        │
        ▼
Zeek Log Generation
        │
        ▼
Traffic Investigation
        │
        ▼
Python Detection Scripts
        │
        ▼
Incident Report
```

---

# ⚔️ Attack Simulations

---

## 1️⃣ SSH Brute Force Detection

**Attack Tool:** Hydra

### Attack Execution

<p align="center">
<img width="1391" height="237" alt="hydra_bruteforce_attack png" src="https://github.com/user-attachments/assets/5a1cb6cf-f566-4925-9107-8a872d0c3dac" />

</p>

### Zeek Log Analysis

<p align="center">
<img src="Screenshots/brute_force/ssh_connlog_analysis.png" width="850">
</p>

### SSH Authentication Analysis

<p align="center">
<img src="Screenshots/brute_force/ssh_authentication_analysis.png" width="850">
</p>

### Wireshark Analysis

<p align="center">
<img src="Screenshots/brute_force/wireshark_ssh_bruteforce_analysis.png" width="850">
</p>

### Python Detection

<p align="center">
<img src="Screenshots/brute_force/bruteforce_detector_alert.png" width="850">
</p>

---

## 2️⃣ TCP SYN Port Scan Detection

**Attack Tool:** Nmap

### Attack Execution

<p align="center">
<img src="Screenshots/port_scan/nmap_syn_scan_execution.png" width="850">
</p>

### Zeek Connection Analysis

<p align="center">
<img src="Screenshots/port_scan/portscan_connlog_analysis.png" width="850">
</p>

### Wireshark Investigation

<p align="center">
<img src="Screenshots/port_scan/wireshark_aggressive_syn_scan.png" width="850">
</p>

### Python Detection

<p align="center">
<img src="Screenshots/port_scan/port_scan_detector_alert.png" width="850">
</p>

---

## 3️⃣ DNS Anomaly Detection

### DNS Query Generation

<p align="center">
<img src="Screenshots/dns_anomaly/dns_query_generation.png" width="850">
</p>

### Zeek DNS Analysis

<p align="center">
<img src="Screenshots/dns_anomaly/dns_log_analysis.png" width="850">
</p>

### Python Detection

<p align="center">
<img src="Screenshots/dns_anomaly/dns_anomaly_alert.png" width="850">
</p>

---

# 📊 Key Features

- SOC-oriented attack simulation
- Network packet capture using tcpdump
- Zeek log investigation
- Wireshark packet analysis
- SSH brute-force detection
- TCP SYN port scan detection
- DNS anomaly detection
- Custom Python detection scripts
- Incident reporting
- Professional GitHub documentation

---

# 📁 Important Zeek Logs

- conn.log
- ssh.log
- dns.log

---

# 🧠 Skills Demonstrated

- Network Traffic Analysis
- Security Monitoring
- Threat Detection
- Zeek Log Analysis
- Wireshark Investigation
- Packet Capture
- Python Automation
- Incident Response
- Blue Team Operations
- SOC Analysis

---

# 🚀 Future Improvements

- HTTP Traffic Analysis
- Malware Traffic Detection
- SIEM Integration (Wazuh / Elastic)
- Email Alerting
- Real-time Detection Dashboard
- MITRE ATT&CK Mapping

---

# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Ashiwan**

Cybersecurity Enthusiast | SOC Analyst Aspirant | Python | Network Security
