from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	await message.reply('Hi')

@dp.message_handler(commands=['command'])
async def echo(message : types.Message):
	await message.answer(message.text)


# @dp.message_handler(lambda message : 'taxi' in message.text)
# async def taxi(message: types.Message):
# 	await message.answer('taxi')


@dp.message_handler(lambda message : 'UFO' in message.text)
async def ufo(message: types.Message):
	await message.answer('UFO')


@dp.message_handler(lambda message : message.text.startswith('taxi'))
async def taxi_number(message: types.Message):
	await message.answer(message.text[5:])


@dp.message_handler()
async def empty(message : types.Message):
	await message.answer('There is no such command')
	await message.delete()

executor.start_polling(dp, skip_updates=True)