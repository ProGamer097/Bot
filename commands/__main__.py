from pyrogram import Client
import asyncio
import os
from config.config import LOGGER, BOT_TOKEN, API_HASH, API_ID, SUPPORT_ID, ERROR_ID
from config.config import DOWNLOAD_DIRECTORY

async def load_start():
    LOGGER.info("[INFO]: STARTING>>>>>.....")

    try:
        aa = random.randint(1, 9)
        await pbot.send_message(
            int(SUPPORT_ID), f"Zoro is UP!!\nTime taken: 0.{aa}"
        )

        g = await pbot.send_message(ERROR_ID, f"Pyrogram Client Started Successfully!!")

        LOGGER.info("[INFO]: PYROGRAM BOT STARTED")

    except Exception as e:
        LOGGER.info(f">>>>>>>>>>>>>>>Bot wasn't able to send message in your log channel\n\nERROR: {e}")

    try:
        await g.delete()
    except:
        LOGGER.info("Deletion Failled!!!!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(load_start())

    app = Client(
        "NANO",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        workers=min(32, os.cpu_count() + 4),
        workdir=DOWNLOAD_DIRECTORY,
        sleep_threshold=60,
        in_memory=True,
        plugins={
            "root": "commands",  # Adjust the path to your commands directory
        },
    )
    
    app.start()

    idle()
    loop.close()
