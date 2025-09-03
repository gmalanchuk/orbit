from aiogram import F, Router
from aiogram.types import Message

from src.constants import constants
from src.keyboards.admin import admin_keyboard


admin_router = Router()


@admin_router.message(F.text.lower() == constants.ADMIN.lower())
async def admin_command(message: Message):
    await message.answer(text="Hello Admin!", reply_markup=admin_keyboard)
