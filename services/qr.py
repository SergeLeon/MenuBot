import io

import qrcode


def as_str(data) -> str:
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)

    temp = io.StringIO()
    qr.print_ascii(out=temp)
    temp.seek(0)

    return temp.read()


def as_bites(data) -> io.BytesIO:
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)

    temp = io.BytesIO()

    qr.make(fit=True)

    img = qr.make_image()
    img.save(temp)
    return temp
