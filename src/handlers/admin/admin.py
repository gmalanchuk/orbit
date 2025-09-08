from aiogram import F, Router
from aiogram.types import Message

from src.constants import constants
from src.keyboards.admin.admin import admin_keyboard


admin_router = Router()


@admin_router.message(F.text.lower() == constants.ADMIN.lower())
async def admin_command(message: Message):
    await message.answer(
        text="Ласкаво просимо в адмін-панель!\n"
        "Тут ти можеш створити новий офер або переглянути статистику вже існуючих😎",
        reply_markup=admin_keyboard,
    )
