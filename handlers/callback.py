

#
#
# import pickle
# from aiogram import Bot, Dispatcher, types, exceptions
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

