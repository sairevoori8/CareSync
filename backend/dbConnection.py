from pymongo import MongoClient
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("KEY")
#mongourl = os.getenv("MongoConnection")
mongourl = "mongodb://localhost:27017"
print(mongourl)

def get_db():
    
    uri = mongourl
    client = MongoClient(uri)

    try:
        client.admin.command("ping")
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


    db = client["Medical"]
    return db

def get_cipher():
    return Fernet(SECRET_KEY)
