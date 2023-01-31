from telegram.ext.filters import MessageFilter

from handlers.response import get_chat_id

admins = set()


class Filter(MessageFilter):
    @staticmethod
    def check_update(update):
        return get_chat_id(update) in admins


def create(user_id) -> None:
    admins.add(user_id)


def delete(user_id) -> None:
    admins.remove(user_id)


def get_all() -> tuple:
    return tuple(admins)
