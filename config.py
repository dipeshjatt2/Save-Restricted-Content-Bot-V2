# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22118129"))
API_HASH = getenv("API_HASH", "43c66e3314921552d9330a4b05b18800")
BOT_TOKEN = getenv("BOT_TOKEN", "6530435719:AAHAWHqESgxbjZWVfaN8eM6eqXAMA_sWVxo")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5203820046").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://syangshibo1:mongodbdatabase500@cluster0.vtkrte7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002222653787")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002227337760"))
