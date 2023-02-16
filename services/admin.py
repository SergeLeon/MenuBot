import json

from telegram.ext.filters import MessageFilter

from handlers.response import get_chat_id
import logger

logger = logger.get_logger(__name__)


def save_admins():
    with open("admins.json", "w") as fp:
        json.dump(admins, fp)


def read_admins() -> list:
    with open("admins.json", "r") as fp:
        return json.load(fp)


try:
    admins = read_admins()
except FileNotFoundError:
    admins = list()


class Filter(MessageFilter):
    @staticmethod
    def check_update(update):
        return is_admin(get_chat_id(update))


def create(user_id) -> None:
    assert not is_admin(user_id), "User is already an admin"
    admins.append(user_id)
    save_admins()
    logger.debug(f"Added admin: {user_id}")


def delete(user_id) -> None:
    admins.remove(user_id)
    save_admins()
    logger.debug(f"Deleted admin: {user_id}")


def get_all() -> list:
    return admins.copy()


def is_admin(user_id):
    return user_id in admins
