import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, ChatWriteForbidden, FloodWait

# Configuration Class
class Config:
    BOT_TOKEN = "8122656092:AAEmh5hWSYOo_Y9DCSD7rvDnvBvMGGogreM"
    API_ID = "11970346"
    API_HASH = "bf43ff670be15fd740eed94820fdd49f"
    CHANNEL = [
        "-1002386644256:-1002484982348",
        "-1001597273610:-1001721796359",
        "-1002100804603:11112222444455",
        "-1002100804603:-1002334248978"
    ]  # Add multiple mappings as needed

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
@bot.on_message(filters.channel & filters.video)
async def forward_media(client, message):
    try:
        if message.video and (message.video.mime_type == "video/x-matroska" or message.video.mime_type == "video/mp4"):
            for mapping in Config.CHANNEL:
                source, destination = mapping.split(":")
                if str(message.chat.id) == source:
                    try:
                        await asyncio.sleep(0.5)  # Throttle forwarding to avoid limits
                        await message.copy(int(destination))
                        logger.info(f"Forwarded video from {source} to {destination}")
                    except ChatWriteForbidden:
                        logger.error(f"Bot cannot write to destination: {destination}. Check permissions.")
                    except PeerIdInvalid:
                        logger.error(f"Invalid peer ID for destination: {destination}. Check configuration.")
                    except FloodWait as e:
                        logger.warning(f"Rate limit exceeded. Waiting for {e.value} seconds.")
                        await asyncio.sleep(e.value)  # Wait and retry
    except Exception as e:
        logger.error(f"Error while forwarding: {e}")

# Run Bot
if __name__ == "__main__":
    bot.run()
