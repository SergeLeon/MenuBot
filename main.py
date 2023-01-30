import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

import config
import handlers
from services import auth

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()
    # TODO: Разобраться как вытащить имя бота
    # auth.print_qr(auth.generate_invite(bot_name))

    COMMAND_HANDLERS = (
        CommandHandler(callback=handlers.start, command="start"),
        CommandHandler(callback=handlers.edit_menu, command="edit"),
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
