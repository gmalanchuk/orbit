from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.handlers.admin.admin import admin_command


cancel_router = Router()


@cancel_router.message(Command(commands=["cancel"]))
async def cancel_command(message: Message, state: FSMContext):
    await state.clear()
    return await admin_command(message)
