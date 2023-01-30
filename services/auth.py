from uuid import uuid4
import qrcode


def _generate_code() -> str:
    # TODO: Сохранять сгенерированный код для последующей авторизации админа
    code = uuid4()
    return str(code)


def generate_invite(bot_name: str) -> str:
    invitation_code = _generate_code()
    return f"https://t.me/{bot_name}?start={invitation_code}"


def check_code(code) -> bool: ...


def print_qr(data) -> None:
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)
    qr.print_ascii()
