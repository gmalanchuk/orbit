from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.constants import constants


kb = [
    [KeyboardButton(text=constants.MAIN_MENU)],
]

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
