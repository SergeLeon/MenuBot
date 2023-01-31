import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

import config
import handlers

from services import admin, auth, qr

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def first_init():
    admin_invite = auth.generate_invite()
    print(admin_invite)
    print(qr.as_str(admin_invite))


def main():
    first_init()

    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    COMMAND_HANDLERS = (
        CommandHandler(callback=handlers.start, command="start"),

        CommandHandler(callback=handlers.edit_menu, command="edit", filters=admin.Filter),
        CommandHandler(callback=handlers.add_admin, command="hire", filters=admin.Filter),
        CommandHandler(callback=handlers.delete_admin, command="fire", filters=admin.Filter),

        MessageHandler(callback=handlers.send_menu, filters=filters.BaseFilter()),
    )
    for handler in COMMAND_HANDLERS:
        application.add_handler(handler)

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
