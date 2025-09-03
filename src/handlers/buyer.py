from aiogram import Router, F
from aiogram.types import Message

buyer_router = Router()


@buyer_router.message(F.text.lower() == "трафер")
async def admin_command(message: Message):
    await message.answer(text="Hello Buyer!")
