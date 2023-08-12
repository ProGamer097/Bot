import logging
from pyrogram import Client
from zoro_bot.config.config import API_ID, API_HASH, BOT_TOKEN

# Import commands from each module
from commands import start, bounty, crew, fight, passive, topcrews, xinfo, xtop, other_commands
from database import init

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create the Pyrogram client
app = Client("zoro_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    try:
        # Load modules
        init()  # Initialize the database
        
        # Load command modules
        start.load(app)
        bounty.load(app)
        crew.load(app)
        fight.load(app)
        passive.load(app)
        topcrews.load(app)
        xinfo.load(app)
        xtop.load(app)
        other_commands.load(app)
        
        # Run the Pyrogram client
        app.start()

        # Stop the Pyrogram client on program termination
        app.stop()
        
        # Send a deployment successful message
        with app:
            app.send_message("your_chat_id", "Zoro Bot has been deployed successfully!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
