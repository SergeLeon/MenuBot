from typing import Iterable, Callable

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes

from handlers.response import send_response


async def send_choice(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        callback_prefix: str,
        title: str,
        items: Iterable,
        to_string: Callable = None,
) -> None:
    keyboard = get_keyboard(items, callback_prefix, to_string)
    await send_response(update, context, title, keyboard)


async def edit_choice(
        query,
        items: Iterable,
        callback_prefix: str,
        to_string: Callable = None,
        text: str = None
) -> None:
    keyboard = get_keyboard(items, callback_prefix, to_string)
    message = query.message

    if message.text == text and message.reply_markup == keyboard:
        return

    if not text:
        text = query.message.text
    await query.edit_message_text(text=text, reply_markup=keyboard)


def get_keyboard(
        items: Iterable,
        callback_prefix: str,
        to_string: Callable
) -> InlineKeyboardMarkup:
    if to_string is None:
        to_string = str

    buttons = [
        [
            InlineKeyboardButton(
                text=to_string(item),
                callback_data=f"{callback_prefix}{index}")
        ]
        for index, item in enumerate(items)
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard


async def get_user_choice(query, prefix: str) -> str | None:
    if not _check_query(query):
        return None
    user_choice = query.data.replace(prefix, "")
    return user_choice


async def get_query(update: Update):
    query = update.callback_query
    await query.answer()
    return query


def _check_query(query) -> bool:
    return query.data and query.data.strip()
