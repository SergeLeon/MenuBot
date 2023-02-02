from telegram import Update
from telegram.ext import ContextTypes

from services import admin, auth, qr
from .response import send_response, get_chat_id


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    admin_invite = auth.generate_invite()
    await send_response(update, context, f"Приглашение админа:\n{admin_invite}")
    await context.bot.send_photo(user_id, qr.as_bites(admin_invite).getvalue())


async def delete_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ...


async def init_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    admin.create(user_id)
    await send_response(update, context, "Пользователь инициализирован как админ")
