from pyrogram import filters, Client
from database.database import db

# Assuming db is your database connection
characters_collection = db["characters"]

@Client.on_message(filters.command("addz") & filters.user("admin_id"))
async def add_character_command(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        char_id = splitted[0]
        anime_id = splitted[1]
        url = splitted[2]
        name = text.split(None, 1)[1].split(None, 1)[1].split(None, 1)[1]
    except:
        return await message.reply_text("Format:\n`/addz (character id) (anime id) (url) (name)`")
    
    character_data = {
        "char_id": char_id,
        "anime_id": anime_id,
        "url": url,
        "name": name
    }

    characters_collection.insert_one(character_data)
    await message.reply_text(f"Character '{name}' has been added to the database.")

@Client.on_message(filters.command("zlist"))
async def character_list_command(client, message):
    characters = characters_collection.find()
    
    if characters.count() == 0:
        await message.reply_text("No characters found in the database.")
        return
    
    character_list = "\n".join([f"ID: {char['char_id']}, Name: {char['name']}, Url: {char['url']}" for char in characters])
    await message.reply_text(f"Character List:\n{character_list}")
