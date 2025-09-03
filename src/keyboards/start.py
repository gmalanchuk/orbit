from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = [
    [
        KeyboardButton(text='Адмін'),
        KeyboardButton(text='Трафер')
    ]
]

start_keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, is_persistent=True)
