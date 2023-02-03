from telegram import Update
from telegram.ext import ContextTypes

import config
from services import admin, auth, qr
from .response import send_response, get_chat_id
from .choice import send_choice, edit_choice, get_user_choice, get_query


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    admin_invite = auth.generate_invite()
    await send_response(update, context, f"Приглашение админа:\n{admin_invite}")
    await context.bot.send_photo(user_id, qr.as_bites(admin_invite).getvalue())


async def delete_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admins = admin.get_all()
    await send_choice(
        update=update,
        context=context,
        callback_prefix=config.ADMIN_DELETE_CALLBACK_PATTERN,
        title="Выбор админа для удаления",
        items=admins,
    )


async def delete_admin_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    if not admin.is_admin(user_id):
        await send_response(update, context, f"Недостаточно полномочий.")
        return

    query = await get_query(update)
    user_choice = await get_user_choice(query, config.ADMIN_DELETE_CALLBACK_PATTERN)
    admin_id = admin.get_all()[user_choice]
    if admin_id == user_id:
        await update_delete_admin_button(query, f"Нельзя разжаловать себя.")
    else:
        admin.delete(admin_id)
        await update_delete_admin_button(query, f"Админ {admin_id} разжалован.")


async def update_delete_admin_button(query, text: str):
    admins = admin.get_all()
    await edit_choice(
        query=query,
        items=admins,
        callback_prefix=config.ADMIN_DELETE_CALLBACK_PATTERN,
        text=text
    )


async def init_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    admin.create(user_id)
    await send_response(update, context, "Пользователь инициализирован как админ")
