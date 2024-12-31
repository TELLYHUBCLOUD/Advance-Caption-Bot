from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5056925533"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "23241238"))
API_HASH = str(getenv("API_HASH", "e6ff6e3068dbea75500865ac49c3608f"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7165570655:AAFScTnBANvreZYuyR8TX0QPtToTspp0Qek"))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002009012734") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://seyov22189:seyov22189@cluster0.rttekkf.mongodb.net/?retryWrites=true&w=majority",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `File Name: {file_name}`\n\nSize: {file_size}</b>",
    )
)
