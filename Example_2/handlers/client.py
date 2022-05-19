from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Bon appetit!', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Communication with the bot via PM, write to him: \nhttps://t.me/PiZzAsHeEf777Bot')

# @dp.message_handler(commands=['Opening_hours'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Sun-Thurs from 9:00 to 20:00, Fri-Sat from 10:00 to 23:00')

# @dp.message_handler(commands=['Address'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'st. Sausage 15')

# @dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])	
	dp.register_message_handler(pizza_open_command, commands=['Opening_hours'])
	dp.register_message_handler(pizza_place_command, commands=['Address'])
	dp.register_message_handler(pizza_menu_command, commands=['Menu'])

