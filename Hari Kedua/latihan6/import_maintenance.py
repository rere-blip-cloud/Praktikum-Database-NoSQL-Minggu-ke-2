import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["latihan6"]         
collection = db["maintenance"]  

data = pd.read_csv("maintenance.csv") 

data["tanggal"] = pd.to_datetime(data["tanggal"])

records = data.to_dict(orient="records")
collection.insert_many(records)

print(f"Berhasil insert {len(records)} data dari maintenance.csv ke database latihan6")