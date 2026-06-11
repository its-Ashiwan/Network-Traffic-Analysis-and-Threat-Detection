# Port Scan Analysis – SOC Investigation Report

## Overview

This investigation focuses on detecting and analyzing TCP reconnaissance activity within a controlled virtual lab environment. The objective was to identify suspicious network behavior using Zeek logs, validate findings through packet analysis, and develop a custom detection mechanism capable of identifying port scanning activity without relying on predefined attacker information.

---

## Lab Environment

| System     | Role                           |
| ---------- | ------------------------------ |
| Kali Linux | Attack Simulation System       |
| Windows 11 | Target Host                    |
| Ubuntu     | Monitoring and Analysis System |

The systems were connected through an isolated Host-Only network to ensure safe testing and accurate traffic monitoring.

---

## Investigation Objective

The primary objective was to determine whether any host on the network was performing reconnaissance by probing multiple TCP ports on another system.

Rather than assuming the attack source, the investigation began by analyzing Zeek network telemetry to identify suspicious behavior.

---

## Evidence Collection

The following evidence sources were collected during the investigation:

* Zeek `conn.log`
* Packet Capture (PCAP)
* Wireshark Traffic Analysis
* Nmap Scan Output
* Custom Python Detection Script

All artifacts were preserved for validation and reporting purposes.

---

## Initial Detection

Analysis of Zeek `conn.log` revealed a single source host initiating connections to a large number of destination ports on the Windows target.

### Key Findings

* Multiple TCP connection attempts observed.
* Single source communicating with numerous destination ports.
* Reconnaissance behavior identified.
* Activity exceeded normal user-generated traffic patterns.

The source host was flagged as suspicious and selected for further investigation.

---

## Connection Analysis

Further examination of Zeek connection records showed repeated connection attempts across a wide port range.

Observed characteristics:

* High number of unique destination ports.
* Short connection durations.
* Numerous rejected connections.
* Minimal successful service interactions.

These indicators strongly suggested automated scanning activity rather than legitimate user behavior.

---

## Service Verification

After identifying the suspicious activity, targeted service verification was performed to determine which ports were actively responding on the Windows host.

The verification process confirmed the presence of several accessible services, including remote administration and Windows networking services.

This step helped distinguish open services from closed ports and validated the reconnaissance findings.

---

## Packet-Level Validation

Wireshark analysis was used to validate the behavior observed in Zeek logs.

The packet capture demonstrated:

* Repeated TCP SYN packets.
* Rapid changes in destination ports.
* SYN/SYN-ACK exchanges for responsive services.
* Rejected and reset responses for unavailable ports.

The packet-level evidence matched the connection patterns observed in Zeek telemetry.

---

## Automated Detection

To automate future detection, a Python-based port scan detector was developed.

### Detection Logic

The script:

1. Reads Zeek `conn.log`.
2. Tracks unique destination ports per source host.
3. Compares observed activity against a configurable threshold.
4. Generates alerts when excessive port enumeration is detected.

### Alert Output

The detector successfully identified the scanning host and generated a high-severity alert based on abnormal port enumeration behavior.

This approach simulates how SOC analysts build custom detections from network telemetry.

---

## MITRE ATT&CK Mapping

| Tactic    | Technique                 | ID    |
| --------- | ------------------------- | ----- |
| Discovery | Network Service Discovery | T1046 |

The observed behavior aligns with reconnaissance activity performed to identify accessible network services.

---

## Security Impact

Port scanning does not directly compromise a system; however, it provides attackers with information required for later stages of an attack.

Information gathered during reconnaissance can be used to:

* Identify exposed services.
* Discover administrative interfaces.
* Locate vulnerable applications.
* Plan future exploitation attempts.

For this reason, reconnaissance activity should be investigated and monitored even when no exploitation is observed.

---

## Recommended Actions

* Monitor excessive destination-port enumeration.
* Restrict unnecessary exposed services.
* Correlate reconnaissance events with authentication logs.
* Investigate repeated scanning activity from the same host.
* Preserve network evidence for timeline reconstruction.

---

## Conclusion

The investigation successfully identified and validated TCP port scanning activity using Zeek logs, packet captures, and custom detection logic. The workflow followed a SOC-oriented approach consisting of evidence collection, log analysis, packet validation, service verification, and alert generation.

This case demonstrates how reconnaissance activity can be detected and investigated using network telemetry without prior knowledge of the attack source, closely reflecting real-world SOC operations.
