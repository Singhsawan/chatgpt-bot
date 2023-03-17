from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "16445683"))
API_HASH = getenv("API_HASH", "d0852e13eee2389ff2d9183b00649547")
BOT_TOKEN = getenv("BOT_TOKEN", "6167771101:AAEOY1EnrD3gcqHzv5_snw8Wqxz4BjwNnDI")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
