from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["test_db"]
user_collection = db["users"]
