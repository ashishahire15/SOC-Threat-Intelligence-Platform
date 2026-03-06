import requests
from config import API_KEY

headers = {
    "x-apikey": API_KEY
}

def check_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    response = requests.get(url, headers=headers)
    data = response.json()
    score = data['data']['attributes']['last_analysis_stats']['malicious']
    return score

def check_hash(hash_value):
    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"
    response = requests.get(url, headers=headers)
    data = response.json()
    score = data['data']['attributes']['last_analysis_stats']['malicious']
    return score

def check_domain(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    response = requests.get(url, headers=headers)
    data = response.json()
    score = data['data']['attributes']['last_analysis_stats']['malicious']
    return score
