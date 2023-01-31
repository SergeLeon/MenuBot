from uuid import uuid4
from config import BOT_NAME

codes = []


def _generate_code() -> str:
    code = str(uuid4())
    codes.append(code)
    return code


def generate_invite() -> str:
    invitation_code = _generate_code()
    return f"https://t.me/{BOT_NAME}?start={invitation_code}"


def check_code(code: str) -> bool:
    if code in codes:
        codes.remove(code)
        return True
    return False
