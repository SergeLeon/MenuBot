from telegram.ext.filters import MessageFilter

from handlers.response import get_chat_id
import logger

logger = logger.get_logger(__name__)

admins = set()  # TODO: Сделать сохранение админов


class Filter(MessageFilter):
    @staticmethod
    def check_update(update):
        return get_chat_id(update) in admins


def create(user_id) -> None:
    admins.add(user_id)
    logger.debug(f"Added admin: {user_id}")


def delete(user_id) -> None:
    admins.remove(user_id)
    logger.debug(f"Deleted admin: {user_id}")


def get_all() -> tuple:
    return tuple(admins)
