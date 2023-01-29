import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB_FILE = BASE_DIR / "db.sqlite3"

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

MENU_CSV = os.environ.get('MENU_CSV')
