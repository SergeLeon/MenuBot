from telegram import Update
from telegram.ext import ContextTypes

from services import auth

from .menu import send_menu
from .admin import init_admin


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = _get_code(update)
    if code and auth.check_code(code):
        await init_admin(update, context)
    else:
        await send_menu(update, context)


def _get_code(update: Update) -> str:
    text = update.message.text
    if " " in text:
        return text.split()[1]
    return ""
