import pandas as pd
import os

def risk_level(score):

    if score >= 20:
        return "CRITICAL"
    elif score >= 10:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"


def generate_report(ip, ip_score, hash_value, hash_score, domain, domain_score):

    data = []

    if ip:
        print("\nIndicator:", ip)
        print("Type: IP")
        print("Score:", ip_score)
        print("Risk:", risk_level(ip_score))

        data.append([ip,"IP",ip_score,risk_level(ip_score)])

    if hash_value:
        print("\nIndicator:", hash_value)
        print("Type: Hash")
        print("Score:", hash_score)
        print("Risk:", risk_level(hash_score))

        data.append([hash_value,"Hash",hash_score,risk_level(hash_score)])

    if domain:
        print("\nIndicator:", domain)
        print("Type: Domain")
        print("Score:", domain_score)
        print("Risk:", risk_level(domain_score))

        data.append([domain,"Domain",domain_score,risk_level(domain_score)])

    df = pd.DataFrame(
        data,
        columns=["Indicator", "Type", "Score", "Risk"]
    )

    file_exists = os.path.isfile("report.csv")

    df.to_csv(
        "report.csv",
        mode="a",
        header=not file_exists,
        index=False
    )

    print("Saved to report.csv")
