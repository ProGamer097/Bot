import logging
import time

from pyrogram import Client

API_ID = 14681826  # Your API ID
API_HASH = "add59ab14dbbccf3c92c65ca4477f2fa"  # Your API Hash
BOT_TOKEN = "6206599982:AAGELlIUapiHd88l5z4YuVwXp1h3tHMfotY"  # Your bot token

ERROR_ID = -1001905486162  # private -- Blue Errors log
SUPPORT_CHAT = "NanoSTestingArea"
SUPPORT_ID = -1001905486162  # devslab

DOWNLOAD_DIRECTORY = "./"

MONGO_DB = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"

OWNER_ID = [6198858059]

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
LOGGER.info("DEVELOPED by: @SexyNano")


pbot = Client("hero", API_ID, API_HASH, bot_token=BOT_TOKEN)
pbot.start()

bot = pbot.get_me()
BOT_ID = bot.id
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
BOT_USERNAME = bot.username
