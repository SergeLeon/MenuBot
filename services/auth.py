from uuid import uuid4

from config import BOT_NAME
import logger

logger = logger.get_logger(__name__)

codes = []


def _generate_code() -> str:
    code = str(uuid4())
    _save_code(code)
    return code


def _save_code(code):
    codes.append(code)
    logger.debug(f"Created code: {code}")


def _delete_code(code):
    codes.remove(code)
    logger.debug(f"Deleted code: {code}")


def generate_invite() -> str:
    invitation_code = _generate_code()
    return f"https://t.me/{BOT_NAME}?start={invitation_code}"


def check_code(code: str) -> bool:
    if code in codes:
        _delete_code(code)
        return True
    return False
