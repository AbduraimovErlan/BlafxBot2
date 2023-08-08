from aiogram import types, Dispatcher
from config import bot, dp, users_ids

@dp.message_handler(lambda message: message.chat.type == types.ChatType.PRIVATE)
async def handle_private_messages(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    if "$signal" not in message.text.lower():
        await bot.send_message(744475470, f"Пользователь {user_name} (ID: {user_id}) написал:\n{message.text}")

    if "$signal" in message.text.lower():
        for user_id in users_ids:
            try:
                await bot.forward_message(chat_id=user_id,
                                          from_chat_id=message.chat.id,
                                          message_id=message.message_id)
            except Exception as e:
                await bot.send_message(744475470, f"Не удалось переслать сообщение пользователю с ID {user_id}: {e}")










