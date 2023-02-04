from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

import config
import logger

logger = logger.setup_applevel_logger()

import handlers
from services import admin, auth, qr


def first_admin_init():
    admin_invite = auth.generate_invite()
    print(admin_invite)
    print(qr.as_str(admin_invite))


def main():
    logger.info("Application initialization")

    if not admin.get_all():
        first_admin_init()

    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    HANDLERS = (
        CommandHandler(callback=handlers.start, command="start"),
        CommandHandler(callback=handlers.send_menu, command="menu"),

        CommandHandler(callback=handlers.add_admin, command="hire", filters=admin.Filter),
        CommandHandler(callback=handlers.delete_admin, command="fire", filters=admin.Filter),
        CallbackQueryHandler(callback=handlers.delete_admin_button,
                             pattern=f"{config.ADMIN_DELETE_CALLBACK_PATTERN}.*"),

        CommandHandler(callback=handlers.edit_menu, command="edit", filters=admin.Filter),
        CallbackQueryHandler(callback=handlers.edit_menu_button,
                             pattern=f"{config.EDIT_MENU_CALLBACK_PATTERN}.*"),
        CallbackQueryHandler(callback=handlers.edit_item_button,
                             pattern=f"{config.EDIT_ITEM_CALLBACK_PATTERN}.*"),
        MessageHandler(callback=handlers.edit_item, filters=admin.Filter),

        MessageHandler(callback=handlers.send_menu, filters=filters.BaseFilter()),
    )
    for handler in HANDLERS:
        application.add_handler(handler)

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
