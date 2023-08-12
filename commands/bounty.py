from pyrogram import filters
from database.database import bounties_collection

# Assuming db is your database connection
bounties_collection = db["bounties"]

@Client.on_message(filters.command("bounty"))
async def bounty_command(client, message):
    user_id = message.from_user.id
    add_user(user_id)  # Add user to database
    
    try:
        text = message.text.split(None, 1)[1]
        amount = int(text)
    except:
        return await message.reply_text("Format:\n`/bounty (amount)`")
    
    if amount <= 0:
        return await message.reply_text("Amount must be greater than 0.")
    
    # Update or insert user's bounty amount
    update_bounty(user_id, amount)
    
    await message.reply_text(f"You've added {amount} to your bounty!")

@Client.on_message(filters.command("mybounty"))
async def my_bounty_command(client, message):
    user_id = message.from_user.id
    add_user(user_id)  # Add user to database
    
    bounty = get_bounty(user_id)
    await message.reply_text(f"Your bounty: {bounty}")
