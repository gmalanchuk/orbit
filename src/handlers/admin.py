from aiogram import Router, F
from aiogram.types import Message

admin_router = Router()


@admin_router.message(F.text.lower() == "адмін")
async def admin_command(message: Message):
    await message.answer(text="Hello Admin!")
