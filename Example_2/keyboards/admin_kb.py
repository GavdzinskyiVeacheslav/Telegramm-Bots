from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Admin keyboard buttons

button_load = KeyboardButton('/Download')
button_delete = KeyboardButton('/Delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
	.add(button_delete)