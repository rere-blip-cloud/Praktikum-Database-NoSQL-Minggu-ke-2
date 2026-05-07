import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Memuat konfigurasi dari file .env
load_dotenv()

# Mengambil URI dari .env, jika tidak ada pakai default localhost
uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(uri, serverSelectionTimeoutMS=2000)

try:
    # Cek koneksi
    client.admin.command('ping')
    print("✅ Koneksi MongoDB berhasil!")
except Exception as e:
    print(f"❌ Gagal terhubung: {e}")
finally:
    client.close()