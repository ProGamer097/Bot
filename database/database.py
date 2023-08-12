import pymongo
from pymongo import MongoClient
from zoro_bot.config.config import MONGO_URI, DB_NAME

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]

# Define collections
characters_collection = db["characters"]
bounties_collection = db["bounties"]

# Sample implementation of database functions

# Characters
def upload_character(url, char_id, anime_id, name):
    character_data = {
        "char_id": char_id,
        "anime_id": anime_id,
        "url": url,
        "name": name
    }
    characters_collection.insert_one(character_data)

def get_character_by_id(char_id):
    return characters_collection.find_one({"char_id": char_id})

def get_all_characters():
    return list(characters_collection.find())

# Bounties
def update_bounty(user_id, amount):
    bounties_collection.update_one({"user_id": user_id}, {"$inc": {"amount": amount}}, upsert=True)

def get_bounty(user_id):
    bounty = bounties_collection.find_one({"user_id": user_id})
    return bounty['amount'] if bounty else 0

# Implement other database functions here
