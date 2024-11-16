# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24935727"))
API_HASH = getenv("API_HASH", "3fd33336629324ecd664e9b6894f0909")
BOT_TOKEN = getenv("BOT_TOKEN", "7968743365:AAHvq_JsnLeDWLyB8ah2N0P3Wmw6jHFiYLY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6326227068").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sujay5372192:sujay5372192@cluster00001.zivqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
LOG_GROUP = getenv("LOG_GROUP", "-1002369795937")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002397574322"))
