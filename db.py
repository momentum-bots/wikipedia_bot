import pymongo

config_uri = "mongodb://localhost/wikipedia_bot"
client = pymongo.MongoClient(config_uri)

users_db = client.get_database("users_db")
