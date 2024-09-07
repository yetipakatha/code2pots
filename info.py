import re, os
from os import environ, getenv
from Script import script
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28045580'))
API_HASH = environ.get('API_HASH', '83001e24418ec7f54bfe95d4e390419f')
OWNER_ID = environ.get('OWNER_ID', '655594746')
BOT_TOKEN = environ.get('BOT_TOKEN', "7505385904:AAGJTJHENU6ID3oBWRIOV4dk5_Q5ngnQRUM")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/fa23dfa622d06d0a31afd.jpg https://telegra.ph/file/99426f2cb0ecb918cb99f.jpg https://telegra.ph/file/e7faedcc78e423368c116.jpg https://telegra.ph/file/b14976ce35081fdeddbf0.jpg https://telegra.ph/file/831589cc710bf65d1d33b.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/e7faedcc78e423368c116.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/831589cc710bf65d1d33b.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/99426f2cb0ecb918cb99f.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/347c1f79f36d3cf14e0f5.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/02e7ecc3e2693b481b914.jpg'))
REFER_PICS = (environ.get("REFER_PICS", "https://telegra.ph/file/fa23dfa622d06d0a31afd.jpg https://telegra.ph/file/99426f2cb0ecb918cb99f.jpg")).split()

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'shareus.io'))
STREAM_API = (environ.get('STREAM_API', ''))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/How_to_Download_7x/32'))

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
PREFIX = environ.get("PREFIX", "/")

CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002019622279"))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1556830659').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002038146800').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '0') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002205290340') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002038146800') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False)) # True if you want no results messages in Log Channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://svdmovies:svdmovie123@cluster0.zyckt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#chatgptAI
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")
AI_LOGS = int(environ.get("AI_LOGS", "-1002023597503")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1002019622279').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @we_are_universee</b>")
APPROVED = environ.get("APPROVED_WELCOME", "off").lower()

# Referal Settings
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1 week')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'Soupboy_single') # owner username without @

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002023597503')) #Log channel id ( make sure bot is admin )
DUMP_CHNL = int(environ.get('DUMP_CHNL', '-1002023597503'))

# Verify
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/How_to_Download_7x/26') # How to open tutorial link for verification

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', '1Jh0re6olVUHnr3eEyFG7NZX7RF3')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
BOT_USERNAME = environ.get("BOT_USERNAME", "@SVDmoviesz_bot")
BOT_NAME = environ.get("BOT_NAME", "SVD-MOVINEZ")
BOT_ID = environ.get("BOT_ID", "7505385904")
S_GROUP = environ.get('S_GROUP', "universe_we_are")
S_CHANNEL = environ.get('S_CHANNEL', "we_are_universee")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/universe_we_are')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/we_are_universee')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_to_Download_7x/32') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : Uɴɪᴠᴇʀsᴇ Nᴇᴛᴡᴏʀᴋs')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/SVDmaniamovies') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002038146800')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1001868871195'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
