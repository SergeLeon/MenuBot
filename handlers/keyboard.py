from dataclasses import dataclass
from typing import Iterable

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


@dataclass
class KeyboardButton:
    text: str

    data: str
    callback_prefix: str

    @property
    def callback_data(self) -> str:
        return f"{self.callback_prefix}{self.data}"


def get_keyboard(
        buttons: Iterable[KeyboardButton],
) -> InlineKeyboardMarkup:
    inline_buttons = [
        [
            InlineKeyboardButton(
                text=button.text,
                callback_data=button.callback_data)
        ]
        for button in buttons
    ]
    keyboard = InlineKeyboardMarkup(inline_buttons)
    return keyboard
