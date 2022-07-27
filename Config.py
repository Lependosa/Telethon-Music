import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19584439"))
    API_HASH = os.environ.get("API_HASH", "6d15c23ed0237793e61795a18ea9ecc8")
    BOT_TOKEN = os.environ.get("5498541898:AAEOAzHWnRe8PF09xxjJSXKe6mza8lPPd4I", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Nanamusic")
    SUPPORT = os.environ.get("SUPPORT", "Cari_Temen_Pacar_Online")
    CHANNEL = os.environ.get("CHANNEL", "Ruangkatastory")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dec375214379eeb6e2980.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/a97bee892ad48b4f34e70.jpg")
