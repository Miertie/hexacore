import json
from datetime import datetime

def log(event, data=None):
    entry = {
        "time": str(datetime.now()),
        "event": event,
        "data": data
    }

    with open("logs/app.json", "a") as f:
        f.write(json.dumps(entry) + "\n")