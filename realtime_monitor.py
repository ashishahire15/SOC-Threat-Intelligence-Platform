import time
import json
import time

LOG_FILE = "/var/ossec/logs/alerts/alerts.json"

def monitor_alerts():

    with open(LOG_FILE, "r") as file:

        # move to end of file
        file.seek(0,2)

        while True:

            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            try:
                alert = json.loads(line)
                return alert

            except json.JSONDecodeError:
                continue
