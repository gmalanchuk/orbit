from aiogram import F, Router
from aiogram.types import Message

from src.constants import constants


buyer_router = Router()


@buyer_router.message(F.text.lower() == constants.BUYER.lower())
async def buyer_command(message: Message):
    await message.answer(text="Hello Buyer!")  # todo переписать текст
