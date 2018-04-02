import pymongo
from config import CONFIG_URI

client = pymongo.MongoClient(CONFIG_URI)

users_db = client.get_database()["users_db"]
