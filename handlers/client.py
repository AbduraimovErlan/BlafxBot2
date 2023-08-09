from aiogram import types, Dispatcher
from config import bot, dp, users_ids
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ChatType





@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if user_id not in users_ids:
        users_ids.append(user_id)  # Добавляем ID нового пользователя в список
        await bot.send_message(744475470, f"Новый пользователь начал общение!\nID: {user_id}\nUsername: {user_name}")

    await message.reply("Привет! Я готов помочь Вам.")




@dp.message_handler(commands=['help'], chat_type=ChatType.PRIVATE)
async def help_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="$пригласить друга")
    button2 = types.KeyboardButton(text="$Регистрация логин открыть счет верификация")
    button3 = types.KeyboardButton(text="$Подключить Google Authenticator для защиты и MetaTrader4 для мониторинга")
    button4 = types.KeyboardButton(text="Другая кнопка")
    button5 = types.KeyboardButton(text="Другая кнопка")
    button6 = types.KeyboardButton(text="Другая кнопка")
    button7 = types.KeyboardButton(text="Другая кнопка")
    button8 = types.KeyboardButton(text="Другая кнопка")
    # Добавьте другие кнопки по вашему усмотрению

    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)  # Добавьте сюда остальные кнопки
    await message.reply("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(Text(equals="$пригласить друга"), chat_type=ChatType.PRIVATE)
async def send_youtube_link(message: types.Message):
    youtube_url = "https://youtu.be/v_acSI8ERCM"  # Замените на вашу ссылку на YouTube
    youtube_description = "Когда приглашаете друзей вы можете получить 40% прибыли от их дохода"  # Замените на ваше описание
    response = f"Вот ваша ссылка на YouTube:\n{youtube_url}\n\nОписание:\n{youtube_description}"
    await message.reply(response, disable_web_page_preview=True)

@dp.message_handler(Text(equals="$Регистрация логин открыть счет верификация"), chat_type=ChatType.PRIVATE)
async def send_youtube_link(message: types.Message):
    youtube_url = "https://youtu.be/kK7W6V5wnJA"  # Замените на вашу ссылку на YouTube
    youtube_description = "В данном ролику мы рассмотрим шаг за шагом процесс регистрации и входа в систему, а также " \
                          "расскажем, как открыть свой счет. Узнайте о важности верификации и какие документы могут " \
                          "потребоваться для этого процесса."  # Замените на ваше описание
    response = f"Вот ваша ссылка на YouTube:\n{youtube_url}\n\nОписание:\n{youtube_description}"
    await message.reply(response, disable_web_page_preview=True)

@dp.message_handler(Text(equals="$Подключить Google Authenticator для защиты и MetaTrader4 для мониторинга"), chat_type=ChatType.PRIVATE)
async def send_youtube_link(message: types.Message):
    youtube_url = "https://youtu.be/f1UOLEUuglA"  # Замените на вашу ссылку на YouTube
    youtube_description = "🔐 Google Authenticator: Этот мощный инструмент двухфакторной аутентификации позволяет" \
                          " убедиться, что ваш аккаунт защищен даже в случае, если ваши учетные данные украдены." \
                          " Мы покажем, как настроить Google Authenticator и использовать его для защиты ваших " \
                          "аккаунтов.💼 MetaTrader4 (MT4): Эта популярная торговая платформа широко известна среди" \
                          " трейдеров во всем мире. MT4 обладает мощными инструментами для мониторинга и анализа " \
                          "торговых операций. Мы рассмотрим, как подключить MT4 к вашему брокерскому счету, настроить" \
                          " индикаторы и следить за вашими сделками в реальном времени."  # Замените на ваше описание
    response = f"Вот ваша ссылка на YouTube:\n{youtube_url}\n\nОписание:\n{youtube_description}"
    await message.reply(response, disable_web_page_preview=True)

# from pytube import YouTube
#
# from pytube import YouTube
# import io
#
#
# @dp.message_handler(commands=['send_video'])
# async def send_video_command(message: types.Message):
#     youtube_url = "https://youtu.be/v_acSI8ERCM"  # Замените на вашу фактическую ссылку
#     video = YouTube(youtube_url).streams.get_highest_resolution()
#
#     # Создаем буфер для сохранения видео
#     video_stream = io.BytesIO()
#
#     # Скачиваем видео в буфер
#     video.stream_to_buffer(video_stream)
#
#     # Возвращаем указатель на начало буфера
#     video_stream.seek(0)
#
#     # Отправляем видео через бота
#     await bot.send_video(message.from_user.id, video=video_stream,
#                          caption="Когда приглашаете друзей вы можете получить 40% прибыли от их дохода")


def register_handlers_client(dp: Dispatcher):
    dp.message_handler(commands=['help'])
