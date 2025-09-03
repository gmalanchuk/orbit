from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.keyboards.start import start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text="Hello!", # todo переписать приветственный текст
        reply_markup=start_keyboard
    )
