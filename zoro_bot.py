from pyrogram import Client

API_ID = "19099900"
API_HASH = "2b445de78e5baf012a0793e60bd4fbf5"
BOT_TOKEN = "6206599982:AAGELlIUapiHd88l5z4YuVwXp1h3tHMfotY"

app = Client("zoro_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    app.run()
