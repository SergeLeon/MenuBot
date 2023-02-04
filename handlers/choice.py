from typing import Iterable, Callable

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes

from handlers.response import send_response


async def send_choice(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        text: str,
        callback_prefix: str,
        items: Iterable,
        to_string: Callable = None,
        to_index: Callable = None
) -> None:
    keyboard = get_keyboard(items, callback_prefix, to_string, to_index)
    await send_response(update, context, text, keyboard)


async def edit_choice(
        query,
        text: str,
        callback_prefix: str,
        items: Iterable,
        to_string: Callable = None,
        to_index: Callable = None
) -> None:
    keyboard = get_keyboard(items, callback_prefix, to_string, to_index)
    message = query.message

    if message.text == text and message.reply_markup == keyboard:
        return

    if not text:
        text = query.message.text
    await query.edit_message_text(text=text, reply_markup=keyboard)


def get_keyboard(
        items: Iterable,
        callback_prefix: str,
        to_string: Callable = None,
        to_index: Callable = None
) -> InlineKeyboardMarkup:
    if to_string is None:
        to_string = str

    if to_index is None:
        to_index = enumerate

    buttons = [
        [
            InlineKeyboardButton(
                text=to_string(item),
                callback_data=f"{callback_prefix}{index}")
        ]
        for index, item in to_index(items)
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
