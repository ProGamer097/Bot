import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from commands import start, bounty, upload
from database import init

logging.basicConfig(level=logging.INFO)
app = Client("zoro_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    try:
        init()  
        start.load(app)
        bounty.load(app)
        upload.load(app)      
        app.start()
        app.stop()
        with app:
            app.send_message("-1001905486162", "Zoro Bot has been deployed successfully!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
