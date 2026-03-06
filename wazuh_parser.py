def extract_indicators(alert):

    ip = None
    domain = None
    file_hash = None

    if "data" in alert:
        ip = alert["data"].get("srcip")
        domain = alert["data"].get("domain")
        file_hash = alert["data"].get("hash")

    return ip, domain, file_hash
