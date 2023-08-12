from pyrogram import filters
from database.database import db

# Assuming db is your database connection
users_collection = db["users"]

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id
    user_data = {
        "user_id": user_id
    }
    users_collection.update_one({"user_id": user_id}, {"$setOnInsert": user_data}, upsert=True)
    
    await message.reply_text("Welcome to Zoro Bot! Use /help to see available commands.")

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = (
        "Zoro Bot Help\n"
        "/start - Start using the bot\n"
        "/help - Show this help menu\n"
        "/bounty (amount) - Add bounty to yourself\n"
        "/mybounty - Check your bounty amount\n"
        "/addcharacter (char_id) (anime_id) (url) (name) - Add a character\n"
        "/characterlist - List all characters\n"
        "/addw (waifu_id) (anime_id) (url) (name) - Add a waifu\n"
        "/addh (husbando_id) (anime_id) (url) (name) - Add a husbando\n"
        "/addanime (anime_id) (name) - Add an anime\n"
        "/animelist - List all anime\n"
        "/waifulist - List all waifus\n"
        "/husbandolist - List all husbandos\n"
        "/fight - Fight with other users\n"
        "/passive - Go into passive mode\n"
        "/xinfo - View user information\n"
        "/crew - Create a crew\n"
        "/topcrews - Get top crews\n"
        "/xtop - Alternative to /toppirates"
    )
    await message.reply_text(help_text)
