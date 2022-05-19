from aiogram import types, Dispatcher
from create_bot import dp, bot
import json, string


# @dp.message_handler()
async def echo_send(message : types.Message):
	if { i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
	.intersection(set(json.load(open('cenz.json')))) != set():
		await message.delete()
		await bot.send_message(message.chat.id, f'{message.from_user.first_name} --> Swearing is forbidden!')

def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)
