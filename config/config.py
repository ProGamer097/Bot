import logging
import time

from pyrogram import Client

API_ID = 20457610  # Your API ID
API_HASH = "b7de0dfecd19375d3f84dbedaeb92537"  # Your API Hash
BOT_TOKEN = "7113297786:AAF9HmuUdKTh_Fckjm789QwD3IvcyB7-6DU"  # Your bot token

ERROR_ID = "-1002083898719"  # private -- Blue Errors log
SUPPORT_CHAT = "naruto_support1"
SUPPORT_ID = "-1002083898719"  # devslab

DOWNLOAD_DIRECTORY = "./"

MONGO_DB = "mongodb+srv://vinamratiwari579:m6YDRYH8HbwuEqxt@cluster0.x7ac1wt.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "zoro"


OWNER_ID = [6590287973]

SUDOLIST = []  # REPORTERS
SUPPORTLIST = []  # Inspectors
DEV_LIST = []
DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS  # Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS  # Inspectors

StartTime = time.time()

# enable logging
FORMAT = "[HERO] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[NANO]')
LOGGER.info("ZOROBOT is waking up...")
LOGGER.info("DEVELOPED by: @naruto_of_telegram")


pbot = Client("hero", API_ID, API_HASH, bot_token=BOT_TOKEN)
pbot.start()

bot = pbot.get_me()
BOT_ID = bot.id
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
BOT_USERNAME = bot.username
