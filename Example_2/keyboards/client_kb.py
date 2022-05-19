from aiogram.types import ReplyKeyboardMarkup, KeyboardButton# ,ReplyKeyboardRemove

b1 = KeyboardButton('/Opening_hours')
b2 = KeyboardButton('/Address')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('Share number', request_contact=True)
# b5 = KeyboardButton('Submit where I am', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3)

