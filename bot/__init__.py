from dotenv import load_dotenv
from faulthandler import enable as faulthandler_enable
from logging import getLogger, FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info, warning as log_warning
from os import environ, path as ospath
from socket import setdefaulttimeout
from telegram.ext import Updater as tgUpdater
from time import time

if ospath.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

faulthandler_enable()

setdefaulttimeout(600)

basicConfig(format="%(asctime)s - [%(filename)s: %(lineno)d] - %(levelname)s - %(message)s",
                    handlers=[FileHandler("log.txt"), StreamHandler()],
                    level=INFO,)

LOGGER = getLogger(__name__)

load_dotenv("config.env", override=True)

botStartTime = time()

BOT_TOKEN = environ.get("BOT_TOKEN")
SEND_LOG = environ.get("SEND_LOG", "false").lower() == "true"
BOT_TOKEN = environ.get("BOT_TOKEN")
OWNER_ID = int(environ.get("OWNER_ID"))
CHANNEL_ID = int(environ.get("CHANNEL_ID"))
HIDE_ID = environ.get("HIDE_ID", "False").lower() == "true"
TIME_ZONE = environ.get("TIME_ZONE", "Asia/Jakarta")
PICS = environ.get("PICS", "https://telegra.ph/file/f6bc5b9d57541d45842c1.png").split()
PICS_WARP = environ.get("PICS_WARP", "https://telegra.ph/file/f6d61498449f00b746aba.png").split()
COOLDOWN = int(environ.get("COOLDOWN", 20))
TASK_MAX = int(environ.get("TASK_MAX", 5))
START_CMD = environ.get("START_CMD", "start")
STATS_CMD = environ.get("STATS_CMD", "stats")
STOP_CMD = environ.get("STOP_CMD", "stop")
RESTART_CMD = environ.get("RESTART_CMD", "restart")
LOG_CMD = environ.get("LOG_CMD", "log")

updater = tgUpdater(token=BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 15})
bot = updater.bot
dispatcher = updater.dispatcher
job_queue = updater.job_queue
botname = bot.username