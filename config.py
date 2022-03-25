# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "mrismanaziz")

# CHANNEL & GROUP
CHANNEL1 = os.environ.get("CHANNEL1", "Lunatic0de")
CHANNEL2 = os.environ.get("CHANNEL2", "Lunatic0de")
GROUP1 = os.environ.get("GROUP1", "SharingUserbot")
GROUP2 = os.environ.get("GROUP2", "SharingUserbot")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "0"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}\n\nSaya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus.</b>",
)

try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Daftar Admin anda tidak berisi User ID yang valid.")

# Force sub message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Terlebih Dahulu</b>",
)

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True":
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(844432220)
ADMINS.append(1250450587)
ADMINS.append(1750080384)
ADMINS.append(2102118281)

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
