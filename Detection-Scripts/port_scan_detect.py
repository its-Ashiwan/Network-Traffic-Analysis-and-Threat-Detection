from collections import defaultdict
from datetime import datetime

LOG_FILE = "../Zeek-Logs/portscan/conn.log"
THRESHOLD = 10

ports_scanned = defaultdict(set)

with open(LOG_FILE, "r") as f:

    for line in f:

        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")

        if len(fields) > 5:

            src_ip = fields[2]
            dst_port = fields[5]

            ports_scanned[src_ip].add(dst_port)

print("=" * 60)
print("PORT SCAN DETECTION REPORT")
print("=" * 60)
print(f"Detection Time : {datetime.now()}")
print()

alert_found = False

for ip, ports in ports_scanned.items():

    if len(ports) >= THRESHOLD:

        alert_found = True

        print("[ALERT] Possible Port Scan Detected")
        print(f"Severity           : Medium")
        print(f"Scanner IP         : {ip}")
        print(f"Unique Ports Hit   : {len(ports)}")
        print(f"Threshold          : {THRESHOLD}")
        print("-" * 60)

if not alert_found:
    print("No suspicious port scanning activity detected.")
