from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.handlers.start import start_command


cancel_router = Router()


@cancel_router.message(Command(commands=["cancel"]))
async def cancel_command(message: Message, state: FSMContext):
    return await start_command(message, state)
