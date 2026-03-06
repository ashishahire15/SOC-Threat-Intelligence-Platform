# SOC Threat Intelligence Automation Platform

## Overview

This project is a Python-based SOC automation tool that monitors security alerts and enriches indicators with threat intelligence using the VirusTotal API. The platform continuously analyzes alerts, extracts indicators such as IP addresses, domains, and file hashes, and generates structured investigation reports to assist SOC analysts in faster alert triage.

The system simulates a real SOC workflow by automatically enriching alerts from Wazuh with external threat intelligence.

---

## Architecture

```
Endpoints / Logs
      ↓
Wazuh Agent
      ↓
Wazuh Manager (alerts.json)
      ↓
Python Real-Time Monitor
      ↓
VirusTotal API
      ↓
Threat Intelligence Report (CSV)
```

---

## Features

* Real-time monitoring of security alerts
* Automatic extraction of Indicators of Compromise (IOCs)
* Integration with VirusTotal threat intelligence API
* Risk scoring based on malicious detection counts
* Continuous report generation for SOC investigations
* Modular Python architecture for easy expansion

---

## Technologies Used

* Python 3
* VirusTotal API
* Wazuh SIEM

---

## Project Structure

```
soc-threat-intel-platform/
│
├── main.py
├── realtime_monitor.py
├── wazuh_parser.py
├── vt_lookup.py
├── report_generator.py
├── config.py
├── report.csv
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Ash17171417/soc-threat-intel-platform.git
cd soc-threat-intel-platform
```

Install dependencies:

```
pip install requests pandas
```

---

## Configuration

Create a VirusTotal account and obtain an API key.

Update `config.py`:

```
API_KEY = "YOUR_VIRUSTOTAL_API_KEY"
```

---

## Running the Application

The script monitors the Wazuh alert log located at:

```
/var/ossec/logs/alerts/alerts.json
```

Run the tool:

```
sudo python3 main.py
```

Root privileges may be required because the Wazuh alert logs are restricted.

---

## Example Output

Console output:

```
SOC Threat Intelligence Automation Started...

New Wazuh Alert Detected

Indicator: 185.220.101.5
Type: IP
Score: 12
Risk: HIGH
```

Example `report.csv`:

| Indicator                        | Type | Score | Risk     |
| -------------------------------- | ---- | ----- | -------- |
| 185.220.101.5                    | IP   | 12    | HIGH     |
| 44d88612fea8a8f36de82e1278abb02f | Hash | 45    | CRITICAL |

Each new alert is automatically appended to the report.

---

## SOC Use Case

This project demonstrates how security teams can automate alert enrichment in a SIEM pipeline. By correlating alerts with external threat intelligence sources, analysts can reduce manual investigation time and quickly identify malicious indicators.

---

## Future Improvements

* Integrate additional threat intelligence sources (AbuseIPDB, AlienVault OTX)
* Automated blocking of malicious IPs
* IOC database for historical tracking
* Web dashboard for SOC analysts
* MITRE ATT&CK mapping
* Slack or email alert notifications

---

## License

This project is for educational and research purposes.
