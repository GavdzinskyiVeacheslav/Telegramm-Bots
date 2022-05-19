from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db 

async def on_startup(_):
	print('The bot went online')
	sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)