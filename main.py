from config import Config
from pyrogram import Client, idle
import asyncio, logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")
plugins = dict(root="plugins")

if __name__ == "__main__":
    bot = Client(
        "Master",
        bot_token="8282655063:AAFKE7fkSPMg_nEiaV1gTKY87JK7Jgd-y7s",
        api_id=27433400,
        api_hash="1a286620de5ffe0a7d9b57e604293555",
        sleep_threshold=120,
        plugins="plugins",
        workers=8
    )
    bot.run()

async def main():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} started --->")
    await idle()
    await bot.stop()
    LOGGER.info("<--- Bot Stopped --->")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
