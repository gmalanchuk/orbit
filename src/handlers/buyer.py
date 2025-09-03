from aiogram import Router, F
from aiogram.types import Message

from src.constants import constants

buyer_router = Router()


@buyer_router.message(F.text.lower() == constants.BUYER.lower())
async def admin_command(message: Message):
    await message.answer(text="Hello Buyer!")
