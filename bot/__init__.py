import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "10955060"))
    API_HASH = os.environ.get("API_HASH", "3cf0de3c9a1105c230fcdeea80fdc42a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7075912876:AAEkQAa8YDSGcLZe2T49ARkhNnbSDmS_-")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "hishamsnap_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
