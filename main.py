import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logger.info(f"Starting at {datetime.now()}")

    data = {
        "name": "sample",
        "date": datetime.now().isoformat()
    }

    with open("sample.json", "w") as f:
        json.dump(data,f)

    logger.info(f"Finished at {datetime.now()}")