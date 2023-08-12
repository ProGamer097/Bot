import pymongo
from pymongo import MongoClient
from zoro_bot.config.config import MONGO_URI, DB_NAME

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]

# Define collections
characters_collection = db["characters"]
# Define other collections as needed

# Sample implementation of database functions

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

# Implement other database functions here
# For example, functions to update, delete, or perform other operations

