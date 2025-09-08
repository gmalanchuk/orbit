from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.keyboards.start import start_keyboard
from src.services.user import UserService


start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()

    if message.text == "/start":  # only works when the bot is launched for the first time
        user_service = UserService()
        user = await user_service.get_user(telegram_user_id=message.from_user.id)
        if not user:
            await user_service.create_user(telegram_user_id=message.from_user.id)
        await message.answer(
            text=(
                "Привіт!👋\n"
                "Я бот для пошуку партнерів з УБТ-трафіку.\n\n"
                "🚀Допомагаю траферам легко знаходити цікаві офери, а адмінам - швидко їх розміщувати.\n"
                "Щоб почати роботу, оберіть свою роль нижче:"
            ),
            reply_markup=start_keyboard,
        )
    else:  # when the user returned to the main menu or used the /cancel command
        await message.answer(
            text="text",  # todo change text
            reply_markup=start_keyboard,
        )
