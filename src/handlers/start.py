from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.keyboards.start import start_keyboard
from src.services.user import UserService


start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: Message):
    if message.text == "/start":
        user_service = UserService()
        user = await user_service.get_user(telegram_user_id=message.from_user.id)
        if not user:
            await user_service.create_user(telegram_user_id=message.from_user.id)
    await message.answer(text="Hello!", reply_markup=start_keyboard)  # todo переписать приветственный текст
