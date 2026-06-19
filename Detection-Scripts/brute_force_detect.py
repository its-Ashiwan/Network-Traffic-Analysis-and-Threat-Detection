from collections import Counter
from datetime import datetime

LOG_FILE = "../Zeek-Logs/bruteforce/ssh.log"
THRESHOLD = 5

ip_counter = Counter()

with open(LOG_FILE, "r") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")

        if len(fields) > 2:
            src_ip = fields[2]
            ip_counter[src_ip] += 1

print("=" * 60)
print("SSH BRUTE FORCE DETECTION REPORT")
print("=" * 60)
print(f"Detection Time : {datetime.now()}")
print()

alert_found = False

for ip, count in ip_counter.items():

    if count >= THRESHOLD:

        alert_found = True

        print("[ALERT] SSH Brute Force Activity Detected")
        print(f"Severity      : High")
        print(f"Attacker IP   : {ip}")
        print(f"SSH Attempts  : {count}")
        print(f"Threshold     : {THRESHOLD}")
        print("-" * 60)

if not alert_found:
    print("No suspicious SSH brute-force activity detected.")
