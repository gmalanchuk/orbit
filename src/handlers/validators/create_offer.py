from decimal import Decimal, InvalidOperation

from src.database.models.offer import OfferType
from src.keyboards.offer_type import offer_type_keyboard


async def name_validator(message):
    if len(message.text) > 64:
        return await message.answer(
            text="Назва оферу не може бути довшою за 64 символи. Введіть назву оферу:"
        )  # todo переписать текст ошибки
    return None


async def telegram_channel_url_validator(message):
    if "t.me/" not in message.text:
        return await message.answer(text="Невірне посилання")  # todo переписать текст ошибки
    return None


async def offer_type_validator(message):
    types = [e.value for e in OfferType]
    if message.text not in types:
        return await message.answer(
            text="Будь-ласка вибіреть тип оферу з нижче запропонованих:", reply_markup=offer_type_keyboard
        )  # todo переписать текст ошибки
    return None


async def price_per_subscriber_validator(message):
    try:
        num = Decimal(message.text)
        if num < 0 or num > 9999:
            return await message.answer(
                text="Плата за одного підписника має бути більшою за 0 та меншою за 9999. Введіть плату за одного підписника:"
            )  # todo переписать текст
        elif num.as_tuple().exponent < -2:
            return await message.answer(
                text="Плата за одного підписника має мати не більше двох знаків після коми. Введіть плату за одного підписника:"
            )  # todo переписать текст
    except InvalidOperation:
        return await message.answer(text="Будь-ласка введіть коректне число:")  # todo переписать текст

    return num
