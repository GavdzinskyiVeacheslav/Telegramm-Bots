from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  #ReplyKeyboardRemove

b1 = KeyboardButton('/Оpening_hours')
b2 = KeyboardButton('/Address')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('Share number', request_contact=True)
# b5 = KeyboardButton('Submit where I am', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#kb_client.add(b1).add(b2).insert(b3)
#kb_client.row(b1, b2, b3)
#kb_client.add(b1).row(b2, b3)
kb_client.add(b1).add(b2).add(b3)  #.row(b4, b5)

