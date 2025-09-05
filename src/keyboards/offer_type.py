from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.constants import constants


kb = [[KeyboardButton(text="новини"), KeyboardButton(text="вакансії")]]  # todo убрать дублирование с чойсами

offer_type_keyboard = ReplyKeyboardMarkup(
    keyboard=kb, resize_keyboard=True, is_persistent=True, input_field_placeholder=constants.INPUT_FIELD_PLACEHOLDER
)
