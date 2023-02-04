from typing import cast

import telegram
from telegram import Chat, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def send_response(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    response: str,
    reply_markup=None,
    **kwargs
) -> None:
    args = {
        "chat_id": get_chat_id(update),
        "disable_web_page_preview": True,
        "text": response,
        "parse_mode": telegram.constants.ParseMode.HTML,
    }
    if reply_markup:
        args["reply_markup"] = reply_markup

    await context.bot.send_message(**args, **kwargs)


def get_chat_id(update: Update) -> int:
    return cast(Chat, update.effective_chat).id
