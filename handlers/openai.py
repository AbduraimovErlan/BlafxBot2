from aiogram import types, Dispatcher
from config import bot, dp, users_ids
from decouple import Config, Csv
from config import OPENAI_TOKEN
import openai

openai.api_key = OPENAI_TOKEN

# Дальнейший код для работы с OpenAI





@dp.message_handler()
async def send(message: types.Message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003", # Убедитесь, что это правильный идентификатор модели
            prompt=message.text,
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6
        )
        await message.answer(response['choices'][0]['text'])
    except Exception as e:
        await message.answer(str(e)) # Отправить сообщение об ошибке, если что-то пошло не так



def register_handlers_openai(dp: Dispatcher):
    dp.message_handler()
