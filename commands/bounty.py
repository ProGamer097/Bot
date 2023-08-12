from pyrogram import filters
from zoro_bot.config.config import db

# Assuming db is your database connection
bounties_collection = db["bounties"]

@Client.on_message(filters.command("bounty"))
async def bounty_command(client, message):
    try:
        text = message.text.split(None, 1)[1]
        user_id = message.from_user.id
        amount = int(text)
    except:
        return await message.reply_text("Format:\n`/bounty (amount)`")
    
    if amount <= 0:
        return await message.reply_text("Amount must be greater than 0.")
    
    # Update or insert user's bounty amount
    bounties_collection.update_one({"user_id": user_id}, {"$inc": {"amount": amount}}, upsert=True)
    
    await message.reply_text(f"You've added {amount} to your bounty!")

@Client.on_message(filters.command("mybounty"))
async def my_bounty_command(client, message):
    user_id = message.from_user.id
    bounty = bounties_collection.find_one({"user_id": user_id})
    
    if not bounty:
        await message.reply_text("You don't have a bounty yet.")
    else:
        await message.reply_text(f"Your bounty: {bounty['amount']}")

# Implement other bounty-related commands if needed

