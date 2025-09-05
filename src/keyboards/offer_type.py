from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.constants import constants
from src.database.models.offer import OfferType


def build_keyboard(enum_cls):
    keyboard = []
    row = []
    for name, value in enum_cls.__members__.items():
        if len(row) == 3:
            keyboard.append(row)
            row = []
        row.append(KeyboardButton(text=value.value))
    keyboard.append(row)

    return keyboard


offer_type_keyboard = ReplyKeyboardMarkup(
    keyboard=build_keyboard(OfferType),
    resize_keyboard=True,
    is_persistent=True,
    input_field_placeholder=constants.INPUT_FIELD_PLACEHOLDER,
)
