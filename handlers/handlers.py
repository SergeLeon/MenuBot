from telegram import Update
from telegram.ext import ContextTypes

from .response import send_response
from services.menu import Menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): ...


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE): ...


async def delete_admin(update: Update, context: ContextTypes.DEFAULT_TYPE): ...


async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, str(Menu()))


async def edit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, repr(Menu()))


async def init_admin(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
