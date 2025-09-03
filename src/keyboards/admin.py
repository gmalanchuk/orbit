from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.constants import constants

kb = [
    [
        KeyboardButton(text=constants.CREATE_OFFER),
        KeyboardButton(text=constants.VIEW_OFFERS)
    ],
    [
        KeyboardButton(text=constants.MAIN_MENU)
    ]
]

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    is_persistent=True,
    input_field_placeholder=constants.INPUT_FIELD_PLACEHOLDER
)
