from config import bot, dp
from aiogram import types
from aiogram import Dispatcher


# Хранение результатов
votes = {}

@dp.message_handler(commands=['guess'])
async def start_vote(message: types.Message):
    question = "Какой Ark следующий?"
    options = ["Ark 2", "Ark 3", "Ark 4"]

    poll_message = await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        is_anonymous=False
    )

    votes[poll_message.poll.id] = {'message_id': poll_message.message_id, 'voters': {}, 'options': options}

@dp.poll_answer_handler()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    poll_id = poll_answer.poll_id
    user_id = poll_answer.user.id
    option_id = poll_answer.option_ids[0] if poll_answer.option_ids else None

    if poll_id in votes:
        votes[poll_id]['voters'][user_id] = option_id

@dp.message_handler(commands=['results'])
async def show_results(message: types.Message):
    for poll in votes.values():
        result_text = "Results:\n"
        results_count = [0] * len(poll['options'])

        for user_id, option_id in poll['voters'].items():
            results_count[option_id] += 1
            result_text += f"User {user_id} voted for {poll['options'][option_id]}\n"

        result_text += "\nSummary:\n"
        for i, count in enumerate(results_count):
            result_text += f"{poll['options'][i]}: {count} votes\n"

        await message.reply(result_text)



votes2 = {}

@dp.message_handler(commands=['meet'])
async def start_vote(message: types.Message):
    question1 = "Какой день выбираешь для встречи?"
    options1 = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    question2 = "Во сколько освободишься?\n(NY)---(Москва)---(Бишкек)"
    options2 = ["07:00---14:00---17:00", "08:00---15:00---18:00",
                "09:00---16:00---19:00", "10:00---17:00---20:00", "11:00---18:00---21:00",
                "12:00---19:00---22:00", "13:00---20:00---23:00", "14:00---21:00---00:00"]

    poll_message1 = await bot.send_poll(
        chat_id=message.chat.id,
        question=question1,
        options=options1,
        is_anonymous=False
    )

    votes2[poll_message1.poll.id] = {'message_id': poll_message1.message_id, 'voters': {}, 'options': options1}

    poll_message2 = await bot.send_poll(
        chat_id=message.chat.id,
        question=question2,
        options=options2,
        is_anonymous=False
    )

    votes2[poll_message2.poll.id] = {'message_id': poll_message2.message_id, 'voters': {}, 'options': options2}

@dp.poll_answer_handler()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    poll_id = poll_answer.poll_id
    user_id = poll_answer.user.id
    option_id = poll_answer.option_ids[0] if poll_answer.option_ids else None

    if poll_id in votes2:
        votes2[poll_id]['voters'][user_id] = option_id

@dp.message_handler(commands=['results'])
async def show_results(message: types.Message):
    for poll in votes2.values():
        result_text = "Results:\n"
        results_count = [0] * len(poll['options'])

        for user_id, option_id in poll['voters'].items():
            results_count[option_id] += 1
            result_text += f"User {user_id} voted for {poll['options'][option_id]}\n"

        result_text += "\nSummary:\n"
        for i, count in enumerate(results_count):
            result_text += f"{poll['options'][i]}: {count} votes\n"

        await message.reply(result_text)





def register_handlers_callback(dp: Dispatcher):
    dp.message_handler(commands=['guess'])


#
#
#
# import pickle
# from aiogram import exceptions
# from aiogram.utils import executor
# import asyncio
# from decouple import config
#
#
# ALLOWED_USER_IDS = [5750596488, 744475470]  # Список разрешенных пользователей по ID
#
# # Создаем пустой словарь для хранения правильных ответов
# correct_answers = {}
#
# # Чтение данных из файла (если файл существует)
# try:
#     with open('correct_answers.pkl', 'rb') as f:
#         correct_answers = pickle.load(f)
# except FileNotFoundError:
#     pass
#
# @dp.message_handler(commands=['set_correct_answer'])
# async def set_correct_answer(message: types.Message):
#     user_id = message.from_user.id
#
#     # Проверяем, есть ли ID пользователя в списке разрешенных
#     if user_id in ALLOWED_USER_IDS:
#         args = message.get_args().split()
#         if len(args) == 2:
#             question_number = args[0]
#             correct_answer = args[1]
#             correct_answers[question_number] = correct_answer
#
#             # Сохраняем данные в файл
#             with open('correct_answers.pkl', 'wb') as f:
#                 pickle.dump(correct_answers, f)
#
#             await message.reply(f"Установлен правильный ответ для вопроса {question_number}: {correct_answer}")
#     else:
#         await message.reply("У вас нет прав на выполнение этой команды.")
#
# @dp.message_handler(commands=['guess'])
# async def guess_1(message: types.Message):
#     question_number = "1"  # Номер вопроса
#     question = "What is the forecast now?"
#     answer = [
#         "Ark 2",
#         "Ark 3",
#         "Ark 4",
#     ]
#     poll_message = await bot.send_poll(
#         chat_id=message.from_user.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=[correct_answers],
#         open_period=10,
#         explanation="Стыдно не знать"
#     )
#
#     await asyncio.sleep(9)  # Ждем 10 секунд
#
#     try:
#         poll_data = await bot.stop_poll(chat_id=message.from_user.id, message_id=poll_message.message_id)
#     except exceptions.PollHasAlreadyBeenClosed:
#         poll_data = None
#
#     if poll_data:
#         if poll_data.total_voter_count == 0:
#             await bot.send_message(chat_id=message.from_user.id, text="Стыдно не знать")
#         else:
#             chosen_option_index = poll_data.options[poll_data.correct_option_id].text
#             if chosen_option_index == correct_answers.get(question_number, ""):
#                 await bot.send_message(chat_id=message.from_user.id, text="Правильно! Вы выбрали верный ответ.")
#             else:
#                 await bot.send_message(chat_id=message.from_user.id, text="Неправильно. Попробуйте еще раз.")
#

