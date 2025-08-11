import json
from datetime import datetime


if __name__ == "__main__":

    data = {
        "name": "sample",
        "date": datetime.now().isoformat()
    }

    with open("sample.json", "w") as f:
        json.dump(data,f)