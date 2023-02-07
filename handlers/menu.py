from telegram import Update, ForceReply, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

import config
import message_templates
from services import admin
from services.menu import Menu
from handlers.response import send_response, get_chat_id
from handlers.choice import send_choice, edit_choice, get_user_choice, get_query


async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, str(Menu),
                        reply_markup=ReplyKeyboardMarkup(((message_templates.MENU_BUTTON,),), True))


async def edit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_choice(
        update=update,
        context=context,
        callback_prefix=config.EDIT_MENU_CALLBACK_PATTERN,
        text=message_templates.SELECT_ITEM_TO_EDIT,
        items=Menu,
        to_string=_get_dict_first_and_active_str
    )


async def edit_menu_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    if not admin.is_admin(user_id):
        await send_response(update, context, message_templates.NO_PERMISSION)
        return

    query = await get_query(update)
    user_choice = await get_user_choice(query, config.EDIT_MENU_CALLBACK_PATTERN)

    await update_edit_menu_button(query, int(user_choice), message_templates.SELECT_FIELD_TO_EDIT)


async def update_edit_menu_button(query, chosen_item_index, text: str):
    menu_item = Menu[chosen_item_index]
    await edit_choice(
        query=query,
        items=menu_item,
        callback_prefix=config.EDIT_ITEM_CALLBACK_PATTERN,
        text=text,
        to_string=lambda item: f"{item} : {menu_item[item]}",
        to_index=lambda items: ((f"{chosen_item_index}_{item}", item) for item in items)
    )


async def edit_item_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = get_chat_id(update)
    if not admin.is_admin(user_id):
        await send_response(update, context, message_templates.NO_PERMISSION)
        return

    query = await get_query(update)
    user_choice = await get_user_choice(query, config.EDIT_ITEM_CALLBACK_PATTERN)

    menu_index, field_name = user_choice.split("_")
    await send_response(
        update=update,
        context=context,
        response=message_templates.INPUT_FIELD_VALUE.format(menu_index=menu_index, field_name=field_name),
        reply_markup=ForceReply(input_field_placeholder=field_name))


async def edit_item(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_message = update.message.reply_to_message
    if not reply_message:
        await send_menu(update, context)
        return

    menu_index, field_name = reply_message.text.split()[-2:]
    user_input = update.message.text
    if user_input.isnumeric():
        user_input = int(user_input)

    Menu[int(menu_index)][field_name] = user_input
    Menu.save()

    await send_response(
        update=update,
        context=context,
        response=message_templates.FIELD_IS_SET_TO_VALUE.format(
            menu_index=menu_index,
            field_name=field_name,
            value=user_input)
    )


def _get_dict_first_and_active_str(item):
    values = tuple(item.values())
    string = f"{values[0]} {'✅' if values[-1] else '❌'}"
    return string


def _dict_item_to_str(item):
    return tuple(item.values())[0]
