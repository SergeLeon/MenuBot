from telegram import Update
from telegram.ext import ContextTypes

from .response import send_response
from services.menu import Menu
from services import admin, auth


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = _get_code(update)
    if code and auth.check_code(code):
        print(code)


def _get_code(update: Update):
    return update.message.text.split()[1]


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admin.create()


async def delete_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admin.delete()


async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, str(Menu))


async def edit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, repr(Menu))


async def init_admin(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
