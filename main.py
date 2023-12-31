from aiogram.utils import executor
from config import dp
from handlers import client, callback, openai
import logging






client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
# openai.register_handlers_openai(dp)

openai.register_handlers_transformers(dp)  # Обновленное имя функции


from handlers.extra import *



if __name__ == '__main__':
    from aiogram import executor
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
