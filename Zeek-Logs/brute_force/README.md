# SSH Brute Force Zeek Logs

## Overview

This folder contains the Zeek logs generated during the SSH brute-force attack simulation. These logs were used to identify repeated SSH connection attempts and investigate attacker activity.

---

## Log Files

### conn.log
Contains metadata for every network connection.

**Key Fields**
- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol
- Service
- Connection Duration
- Connection State

**Purpose**

Used to identify repeated SSH connections from the attacker's IP.

---

### ssh.log

Contains SSH protocol information.

**Key Fields**

- Source IP
- Destination IP
- Authentication Status
- SSH Version
- Client Information
- Server Information

**Purpose**

Used to investigate SSH authentication attempts and validate brute-force behavior.

---

## Attack Summary

**Attack Type:** SSH Brute Force

**Attacker Machine:** Kali Linux

**Target Machine:** Ubuntu

**Monitoring Tool:** Zeek

**Detection Method:** Zeek Log Analysis + Python Detection Script

---

## Outcome

The collected Zeek logs confirmed multiple SSH connection attempts from a single source IP, indicating brute-force activity against the target system.
