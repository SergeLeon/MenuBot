from telegram import Update
from telegram.ext import ContextTypes

from .response import send_response
from services.menu import Menu
from services import admin, auth
from handlers.response import get_chat_id


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = _get_code(update)
    if code and auth.check_code(code):
        user_id = get_chat_id(update)
        admin.create(user_id)
        await send_response(update, context, "Пользователь инициализирован как админ")
    else:
        await send_menu(update, context)


def _get_code(update: Update) -> str:
    text = update.message.text
    if " " in text:
        return text.split()[1]
    return ""


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...


async def delete_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...


async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, str(Menu))


async def edit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, repr(Menu))


async def init_admin(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
