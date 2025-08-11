import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info(f"Running job at at {datetime.now()}")