import time, random
from datetime import datetime, UTC
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import logging


load_dotenv()


client = MongoClient('mongodb://localhost:27017')
db = client["piton"]
collection = db["test1"]


# logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("crud_sensor.log"),
        logging.StreamHandler()
    ]
)


try:
    while True:
        doc = {
            "mesin": f"CNC-{random.randint(1,5):02d}",
            "suhu": round(random.uniform(60, 100), 2),
            "getaran": round(random.uniform(0.1, 0.5), 2),
            "timestamp": datetime.now(UTC)
        }


        result = collection.insert_one(doc)


        print(f"[{doc['timestamp']}] Inserted: {doc['mesin']} - {doc['suhu']}°C")


        logging.info(f"Insert berhasil: {result.inserted_id}")


        time.sleep(2)


except Exception as e:
    logging.error(f"Insert gagal: {e}")