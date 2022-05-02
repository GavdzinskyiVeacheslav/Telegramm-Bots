import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/images/HI.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲 Random number")
	item2 = types.KeyboardButton("😊 how are you?")
	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nI am - <b>{1.first_name}</b>, a bot designed to be a guinea pig.".format(message.from_user, bot.get_me()),
	parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	#bot.send_message(message.chat.id, message.text)
	if message.chat.type =='private':
		if message.text == '🎲 Random number':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == "😊 how are you?":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Good", callback_data='good')
			item2 = types.InlineKeyboardButton("Not very good", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, "Excellent and you ?", reply_markup=markup)
		else:
			bot.send_message(message.chat.id, "I don't know what to say 😢")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Here is excellent 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Sometimes it happens 😢')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 how are you?",
                reply_markup=None) 

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='This is a test notification!!!')

	except Exception as e:
		print(repr(e))

#RUN
bot.polling(none_stop=True)