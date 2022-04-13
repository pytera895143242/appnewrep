import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
from loader import dp, bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard


@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    await bot.send_message(chat_id=update.from_user.id, text='Нажми /start')
    text = f'''👋 Привет, {update.from_user.full_name}\n\n<b>Этот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n</b>🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    try:
        await update.approve()
    except:
        pass

    if not database.user_exists(update.from_user.id):
        database.create_user(update.from_user.id, update.from_user.username)


    else:
        pass

    await bot.send_photo(
        photo='https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album',
        caption = text, reply_markup=menu_keyboard.keyboard, chat_id=update.from_user.id)
    await bot.send_message(text='🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard,chat_id = update.from_user.id)
