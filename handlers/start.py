from telegram import Update
from telegram.ext import ContextTypes

import message_templates
from services import auth, admin

from handlers.menu import send_menu
from handlers.admin import init_admin
from handlers.response import get_chat_id, send_response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = _get_code(update)
    if code:
        user_id = get_chat_id(update)
        if admin.is_admin(user_id):
            await send_response(update, context, message_templates.ALREADY_ADMIN)
            return

        if auth.check_code(code):
            await init_admin(update, context)
            return

    await send_menu(update, context)


def _get_code(update: Update) -> str:
    text = update.message.text
    if " " in text:
        return text.split(maxsplit=1)[1]
    return ""
