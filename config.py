import os
from pathlib import Path

from dotenv import load_dotenv
import requests

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB_FILE = BASE_DIR / "db.sqlite3"

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
BOT_NAME = requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe').json()["result"]["username"]

MENU_CSV = os.environ.get('MENU_CSV')
