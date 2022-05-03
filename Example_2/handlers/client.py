from aiogram import types, Dispatcher
from create_bot import dp, bot


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Bon appetit!')
		await message.delete()
	except:
		await message.reply('Сommunication with the bot via PM, write to him:\nhttps://t.me/Pizza_Sheef114455bot')

#@dp.message_handler(commands=['Оpening_hours'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Sun-Thurs from 9:00 to 20:00, Fri-Sat from 10:00 to 23:00')

#@dp.message_handler(commands=['Address'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'st. Sausage 15')


# @dp.message_handler(commands=['Menu'])
# async def pizza_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice {ret[-1]}')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])	
	dp.register_message_handler(pizza_open_command, commands=['Оpening_hours'])	
	dp.register_message_handler(pizza_place_command, commands=['Address'])