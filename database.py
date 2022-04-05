from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient

load_dotenv()

MONGO_CLIENT = os.getenv("MONGO_CLIENT")

cluster = MongoClient(MONGO_CLIENT)


db = cluster["healthapp"]

# the name of the database
device_collection = db["device"]


if __name__ == "__main__":
  
  # Test Cases
  post = {"_id": 0, "patient_assigned": 12,
    "device_type": "temperature",
    "measurement": 98.6,
    "MAC": "30-65-EC-6F-C4-58",
    "purchase_date": "01-01-2001",
    "model_number": 1234,
    "model_name": "temp-o-matic",
    "serial_number": 56789 }

  # a post
  device_collection.insert_one(post)
