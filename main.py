from aiogram.utils import executor
from config import dp
from handlers import client, extra
import logging


client.register_handlers_client(dp)
from handlers.extra import *



if __name__ == '__main__':
    from aiogram import executor
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
