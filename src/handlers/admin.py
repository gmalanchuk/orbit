from aiogram import F, Router
from aiogram.types import Message

from src.constants import constants
from src.keyboards.admin import admin_keyboard
from src.services.user import UserService


admin_router = Router()


@admin_router.message(F.text.lower() == constants.ADMIN.lower())
async def admin_command(message: Message):
    user_service = UserService()

    user = await user_service.get_user(telegram_user_id=message.from_user.id)
    if not user:
        await user_service.create_user(telegram_user_id=message.from_user.id)

    await message.answer(text="Hello Admin!", reply_markup=admin_keyboard)  # todo переписать текст
