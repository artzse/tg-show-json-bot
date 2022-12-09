from app import dp
from aiogram import types

@dp.message_handler(commands=["start", "help"])
async def command_start(msg: types.Message):
    message_to_send = "👋 Добро пожаловать!\n\n*Данный бот возвращает параметры JSON в удобном формате.*\n\nПо всем вопросам обащаться к @artzse.\n\n☀Хорошего дня!"
    await msg.answer(message_to_send, parse_mode="MarkDown")

@dp.message_handler()
async def any_message(msg: types.Message):
    message_to_send = f"*From user:*\n" \
                      f"Message ID: `{msg.message_id}`\n" \
                      f"User ID: `{msg.from_user.id}`\n" \
                      f"Is Bot: `{msg.from_user.is_bot}`\n" \
                      f"First Name: `{msg.from_user.first_name}`\n" \
                      f"Last Name: `{msg.from_user.last_name}`\n" \
                      f"Username: `{msg.from_user.username}`\n" \
                      f"Language code: `{msg.from_user.language_code}`\n\n" \
                      f"*Chat:*\n" \
                      f"ID: `{msg.chat.id}`\n" \
                      f"First Name: `{msg.chat.first_name}`\n" \
                      f"Last Name: `{msg.chat.last_name}`\n" \
                      f"Username: `{msg.chat.username}`\n\n" \
                      f"*Message:*\n" \
                      f"Date: `{msg.date}`\n" \
                      f"Text: `{msg.text}`"
    await msg.answer(message_to_send, parse_mode="MarkDown")