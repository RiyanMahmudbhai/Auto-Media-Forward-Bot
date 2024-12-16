import logging
import asyncio
from pyrogram import Client, filters

# Configuration Class
class Config:
    BOT_TOKEN = "8122656092:AAEmh5hWSYOo_Y9DCSD7rvDnvBvMGGogreM"
    API_ID = "11970346"
    API_HASH = "bf43ff670be15fd740eed94820fdd49f"
    CHANNEL = ["-1002386644256:-1002484982348"]  # Format: "source:destination"

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Media Forward Bot Class
class MediaForwardBot(Client, Config):
    def __init__(self):
        super().__init__(
            name="MediaForwardBot",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        logger.info(f"Bot started as {me.first_name} (@{me.username})")

    async def stop(self):
        await super().stop()
        logger.info("Bot stopped.")

# Initialize Bot
bot = MediaForwardBot()

# Media Filtering
@bot.on_message(filters.channel & (filters.photo | filters.video | filters.audio | filters.document))
async def forward_media(client, message):
    try:
        for mapping in Config.CHANNEL:
            source, destination = mapping.split(":")
            if str(message.chat.id) == source:
                await message.copy(int(destination))
                logger.info(f"Forwarded media from {source} to {destination}")
                await asyncio.sleep(1)  # To prevent flooding
    except Exception as e:
        logger.error(f"Error while forwarding: {e}")

# Run Bot
if __name__ == "__main__":
    bot.run()
