from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from handlers.response import send_response


async def send_choice(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        text: str,
        keyboard: InlineKeyboardMarkup
) -> None:
    await send_response(update, context, text, keyboard)


async def edit_choice(
        query,
        text: str,
        keyboard: InlineKeyboardMarkup
) -> None:
    message = query.message

    if message.text == text and message.reply_markup == keyboard:
        return

    if not text:
        text = query.message.text
    await query.edit_message_text(text=text, reply_markup=keyboard)


async def get_user_choice(query, prefix: str) -> str | None:
    if not _check_query(query):
        return None
    user_choice = query.data.replace(prefix, "")
    return user_choice


def _check_query(query) -> bool:
    return query.data and query.data.strip()


async def get_query(update: Update):
    query = update.callback_query
    await query.answer()
    return query
