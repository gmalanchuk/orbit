from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.keyboards.start import start_keyboard


start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="Hello!", reply_markup=start_keyboard)  # todo переписать приветственный текст
