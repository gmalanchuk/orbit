from aiogram import Router, F
from aiogram.types import Message

from src.constants import constants
from src.handlers.start import start_command

main_menu_router = Router()


@main_menu_router.message(F.text.lower() == constants.MAIN_MENU.lower())
async def main_menu_command(message: Message):
    return await start_command(message)
