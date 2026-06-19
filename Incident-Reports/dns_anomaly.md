# DNS Anomaly Incident Report

## Incident Identification

| Field | Recorded Detail |
|---------|---------|
| Incident ID | NTA-DNS-001 |
| Investigation Area | Network Traffic Analysis – DNS Anomaly Detection |
| Alert Severity | Medium |
| Detection Type | Abnormal DNS Query Activity |
| Analyst Disposition | DNS anomaly detected in controlled lab environment |
| Exfiltration Status | Not confirmed |

---

# 1. Executive Summary

During the DNS anomaly detection phase, unusual DNS activity was observed and analyzed using Zeek logs, packet capture evidence, Wireshark and a custom Python detection script.

The investigation identified a host generating a higher-than-normal volume of DNS requests within a short period of time. The activity was captured, analyzed and validated through multiple sources of evidence.

The observed behaviour was classified as a DNS anomaly because the source system generated repeated DNS requests that deviated from normal network activity patterns.

The purpose of this phase was to demonstrate how Security Operations Center (SOC) analysts can use network telemetry and detection logic to identify suspicious DNS behaviour.

---

# 2. Scope of Investigation

This investigation was conducted to:

- Identify systems involved in the DNS activity.
- Review DNS requests captured by Zeek.
- Validate findings through packet-level analysis.
- Generate automated alerts using Python.
- Preserve evidence for incident reporting.
- Assess whether the activity represented abnormal DNS behaviour.

---

# 3. Environment and Evidence Sources

## Observed Systems

| Component | Role |
|------------|---------|
| Kali Linux | Traffic Generation System |
| Ubuntu Target | DNS Activity Source |
| Ubuntu Monitoring System | Zeek, tcpdump and Wireshark |
| Host-Only Network | Monitoring Environment |

## Evidence Sources

| Evidence Source | Purpose |
|----------------|---------|
| dns.log | DNS transaction analysis |
| dns_anomaly.pcap | Packet-level evidence |
| Wireshark | Traffic validation |
| Python Detector | Automated anomaly detection |

---

# 4. Detection Process

The DNS investigation followed a SOC-style workflow:

1. DNS traffic generation
2. Packet capture using tcpdump
3. Zeek log generation
4. DNS log analysis
5. Wireshark validation
6. Automated detection using Python
7. Incident reporting

<img width="1401" height="883" alt="dns_query_generation png" src="https://github.com/user-attachments/assets/223de329-661f-4944-b837-8c2a23c59007" />

This workflow ensured that all findings could be validated using multiple evidence sources.

---

# 5. Technical Analysis

## Zeek DNS Log Analysis

The Zeek `dns.log` file was reviewed to identify:

- Source hosts generating DNS requests
- Queried domains
- DNS request frequency
- Repeated query activity

The log analysis showed that a single source host generated a noticeable volume of DNS traffic during the monitoring period.

### Evidence

<img width="1704" height="863" alt="dns_log_analysis png" src="https://github.com/user-attachments/assets/4cad5df8-805f-4aed-abc0-15676ce530be" />


---

## Wireshark Packet Analysis

Packet capture evidence was examined using Wireshark.

### Display Filter

```text
dns
```

The packet analysis confirmed:

- DNS query traffic was successfully captured.
- Multiple DNS requests were generated during testing.
- The observed traffic matched the Zeek DNS logs.


## Python Detection

A custom Python script was executed to identify abnormal DNS activity.

The script:

- Parsed Zeek DNS logs.
- Counted DNS requests per source host.
- Compared activity against a predefined threshold.
- Generated alerts for suspicious DNS behaviour.

### Detector Execution

<img width="1712" height="881" alt="detector_alert_execution png" src="https://github.com/user-attachments/assets/204c2e22-de64-4afe-a376-90cbed84d19f" />


### Detection Alert

<img width="1707" height="852" alt="dns_anomaly_alert png" src="https://github.com/user-attachments/assets/3628a540-1e0d-481e-b3f2-dc2ad0b920f2" />


# 6. Investigation Findings

The investigation revealed:

- Increased DNS request activity from a single source host.
- Repeated DNS query generation.
- Successful detection through automated analysis.
- Correlation between Zeek logs and packet captures.

The collected evidence indicated behaviour that differed from normal DNS usage patterns.

---

# 7. Analyst Assessment

The activity was classified as a DNS anomaly because of:

- Elevated DNS request volume.
- Repeated query behaviour.
- Detection script alert generation.
- Consistent evidence across Zeek and Wireshark analysis.

Although the activity was generated in a controlled lab environment, similar behaviour in a production network could warrant further investigation.

Potential causes may include:

- Automated scripts
- Reconnaissance activity
- Malware communication
- DNS tunneling attempts

No evidence of confirmed data exfiltration was identified during this investigation.

---

# 8. Severity Assessment

| Factor | Assessment |
|----------|------------|
| DNS Activity Volume | Elevated |
| Detection Alert | Generated |
| Evidence Validation | Confirmed |
| Impact | Low (Lab Environment) |
| Severity | Medium |

---

# 9. Response Recommendations

If similar activity is detected in a production environment:

- Investigate the source host.
- Review endpoint processes generating DNS traffic.
- Correlate DNS activity with authentication and network logs.
- Monitor DNS request volume for unusual spikes.
- Implement DNS anomaly alerting.
- Preserve packet captures and log evidence.

---

# 10. Final Analyst Conclusion

The DNS anomaly detection phase successfully demonstrated how Zeek, Wireshark and custom Python detection logic can be used to identify suspicious DNS behaviour.

The activity was detected, validated and documented using a structured SOC investigation workflow. While no malicious impact was confirmed in the lab environment, the investigation demonstrated practical threat detection and incident response skills relevant to SOC analyst operations.

The incident was therefore classified as:

**DNS Anomaly Detected – Further Investigation Recommended**



---

# Evidence Reference Index

```text
Incident-Reports/
└── DNS_Anomaly_Report.md

Analysis/
└── DNS_Anomaly_Analysis.md

Detection-Scripts/
└── dns_anomaly_detector.py

PCAP/
└── dns_anomaly/
    └── dns_anomaly.pcap

Zeek-Logs/
└── dns_anomaly/
    └── dns.log

Screenshots/
└── dns_anomaly/
    ├── dns_query_generation.png
    ├── dns_log_analysis.png
    └── dns_anomaly_alert.png
```
