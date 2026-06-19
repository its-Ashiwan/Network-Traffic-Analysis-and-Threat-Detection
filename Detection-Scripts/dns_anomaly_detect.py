from collections import Counter
from datetime import datetime

LOG_FILE = "../Zeek-Logs/dns/dns.log"
THRESHOLD = 20

dns_counter = Counter()

with open(LOG_FILE, "r") as f:

    for line in f:

        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")

        if len(fields) > 9:

            src_ip = fields[2]
            dns_counter[src_ip] += 1

print("=" * 60)
print("DNS ANOMALY DETECTION REPORT")
print("=" * 60)
print(f"Detection Time : {datetime.now()}")
print()

alert_found = False

for ip, count in dns_counter.items():

    if count >= THRESHOLD:

        alert_found = True

        if count >= 100:
            severity = "High"
        elif count >= 50:
            severity = "Medium"
        else:
            severity = "Low"

        print("[ALERT] Suspicious DNS Activity Detected")
        print(f"Severity      : {severity}")
        print(f"Source IP     : {ip}")
        print(f"DNS Queries   : {count}")
        print(f"Threshold     : {THRESHOLD}")
        print("-" * 60)

if not alert_found:
    print("No suspicious DNS activity detected.")
