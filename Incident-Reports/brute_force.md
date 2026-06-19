
# Incident Report: SSH Brute Force Attack

## Incident Summary

During network traffic monitoring, suspicious SSH activity was detected originating from a single host within the lab environment. Multiple authentication attempts were observed against the SSH service running on the target system. The activity was investigated using Zeek logs, Wireshark packet captures and a custom Python detection script.

---

## Environment

| Component | Role |
|------------|---------|
| Kali Linux | Attacker |
| Ubuntu | Target System |
| Ubuntu Monitoring System | Zeek, Wireshark, tcpdump |
| Network Type | Host-Only Network |

---

## Incident Details

| Field | Value |
|---------|---------|
| Incident Type | SSH Brute Force Attack |
| Severity | Medium |
| Source IP | 192.168.111.130 |
| Destination IP | 192.168.111.128 |
| Target Service | SSH |
| Destination Port | 22 |
| Detection Method | Zeek Logs, Wireshark, Python Detector |

---

## Detection Timeline

1. SSH service was enabled on the target system.
2. Hydra was executed from the Kali Linux machine.
3. Network traffic was captured using tcpdump.
4. Zeek generated SSH-related logs.
5. Wireshark analysis confirmed repeated SSH connections.
6. Custom Python detector generated a brute force alert.
7. Investigation confirmed brute force behavior.

---

## Evidence Collected

### Zeek Log Analysis

Zeek logs showed repeated SSH connection attempts from the same source IP address targeting port 22 on the destination host.

Evidence:

<img width="1713" height="871" alt="zeek_bruteforce_investigation png" src="https://github.com/user-attachments/assets/9ce8fba5-20c2-4eaa-ae5b-a76eb9db0317" />



---

### Wireshark Analysis

Wireshark packet analysis revealed multiple TCP SYN packets and SSH handshake attempts between the attacker and target systems.

Evidence:

<img width="1716" height="866" alt="wireshark_ssh_bruteforce_analysis png" src="https://github.com/user-attachments/assets/6960332c-5a40-4d30-9501-262830b3366d" />


---

### Attack Execution

Hydra was used to perform the brute force attack against the SSH service.

Evidence:

<img width="1391" height="237" alt="hydra_bruteforce_attack png" src="https://github.com/user-attachments/assets/dc1d17ea-04d9-445d-8152-71eb2a53cfc3" />


---

### Detection Alert

The custom Python detection script successfully identified excessive SSH connection attempts and generated an alert.

Evidence:

<img width="1710" height="867" alt="python_bruteforce_detection_alert png" src="https://github.com/user-attachments/assets/4c04db2d-81be-4579-b1f3-35fcff45a911" />


---

## Analysis

The traffic pattern indicated automated authentication attempts against the SSH service. A single host repeatedly attempted to establish SSH connections within a short period of time.

Key indicators observed:

- Repeated SSH connection attempts
- Continuous targeting of port 22
- Automated attack behavior
- Consistent source IP activity
- Detection script alert generation

The activity was consistent with SSH brute force behavior and could not be attributed to normal administrative access.

---

## Analyst Verdict

The incident was confirmed as an SSH brute force attack originating from:

Source IP: 192.168.111.130

Target IP: 192.168.111.128

Target Service: SSH (Port 22)

The attack was successfully detected using Zeek logs, packet analysis and custom detection logic.

---

## Recommendations

- Use SSH key-based authentication.
- Disable password-based SSH authentication where possible.
- Implement account lockout policies.
- Restrict SSH access through firewall rules.
- Monitor authentication failures continuously.
- Configure alerts for repeated SSH connection attempts.

---

## Conclusion

The investigation successfully identified and confirmed SSH brute force activity within the lab environment. The attack was detected through a combination of Zeek log analysis, Wireshark packet inspection and a custom Python detection script. This phase demonstrates practical SOC investigation skills including traffic analysis, threat detection and incident reporting.
