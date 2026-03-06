from realtime_monitor import monitor_alerts
from wazuh_parser import extract_indicators
from vt_lookup import check_ip, check_hash, check_domain
from report_generator import generate_report

print("SOC Threat Intelligence Automation Started...\n")

while True:

    alert = monitor_alerts()

    ip, domain, file_hash = extract_indicators(alert)

    if not ip and not domain and not file_hash:
        continue

    print("\n========== NEW WAZUH ALERT ==========")

    ip_score = check_ip(ip) if ip else 0
    hash_score = check_hash(file_hash) if file_hash else 0
    domain_score = check_domain(domain) if domain else 0

    generate_report(ip, ip_score, file_hash, hash_score, domain, domain_score)
