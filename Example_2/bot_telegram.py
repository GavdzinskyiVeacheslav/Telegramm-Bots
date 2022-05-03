import aiogram
from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher 
from aiogram.utils import executor
import os, json, string

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
	print("The bot went online")

'''********************Client part********************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Bon appetit!')
		await message.delete()
	except:
		await message.reply('Сommunication with the bot via PM, write to him:\nhttps://t.me/Pizza_Sheef114455bot')

@dp.message_handler(commands=['Оpening_hours'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Sun-Thurs from 9:00 to 20:00, Fri-Sat from 10:00 to 23:00')

@dp.message_handler(commands=['Address'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'st. Sausage 15')


# @dp.message_handler(commands=['Menu'])
# async def pizza_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[-1]}')
	

'''********************Admin part********************'''
'''********************General part********************'''

@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		await message.delete()
		await bot.send_message(message.chat.id, f'{message.from_user.first_name} --> Swearing is forbidden!')
		
		



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  
