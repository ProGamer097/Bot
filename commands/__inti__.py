# hero/__init__.py

import logging
import time

from pyrogram import Client


API_ID = 14681826  # Your API ID
API_HASH = "add59ab14dbbccf3c92c65ca4477f2fa"  # Your API Hash
BOT_TOKEN = "6206599982:AAGELlIUapiHd88l5z4YuVwXp1h3tHMfotY"  # Your bot token

ERROR_ID = -1001905486162 #private -- Blue Errors log
SUPPORT_CHAT = "NanoSTestingArea"
SUPPORT_ID = -1001905486162 #devslab

DOWNLOAD_DIRECTORY = "./"

#DB_URI = "postgres://cugocwks:jgpqMTLw2rO6KMwnWDL6kAXwmaVMB1qW@john.db.elephantsql.com/cugocwks"
MONGO_DB = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"

OWNER_ID = [6198858059]

SUDOLIST = [] #REPORTERS
SUPPORTLIST = [] #Inspectors
DEV_LIST = []
DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Inspectors


StartTime = time.time()

# enable logging
FORMAT = "[ZORO] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[NANO]')
LOGGER.info("ZOROBOT is waking up...")
LOGGER.info("DEVELOPED by: @SexyNano")


pbot = Client("zoro", API_ID, API_HASH, bot_token=BOT_TOKEN)
pbot.start()

