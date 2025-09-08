from decimal import Decimal, InvalidOperation

from src.database.models.offer import OfferType
from src.keyboards.offer_type import offer_type_keyboard


async def name_validator(message):
    if len(message.text) > 64:
        return await message.answer(
            text="На жаль, наша система не дозволяє давати оферам такі довгі назви. Максимальна кількість символів - 64"
        )
    return None


async def telegram_channel_url_validator(message):
    if "t.me/" not in message.text:
        return await message.answer(
            text="Чомусь система не змогла розпізнати посилання😅\n"
            "Перевір, чи це дійсно посилання на Telegram-канал?"
        )
    return None


async def offer_type_validator(message):
    types = [e.value for e in OfferType]
    if message.text not in types:
        return await message.answer(
            text="У системі є суворі правила щодо типів оферів\n" "Обери, будь ласка, один із запропонованих нижче:",
            reply_markup=offer_type_keyboard,
        )
    return None


async def price_per_subscriber_validator(message):

    # todo message.text.isdigit

    try:
        num = Decimal(message.text)
        if num < 0 or num > 9999:
            return await message.answer(
                text="Плата за одного підписника має бути в діапазоні від 0 до 9999. Спробуй ще раз:"
            )
        elif num.as_tuple().exponent < -2:
            return await message.answer(text="Можна вказати лише два знаки після коми. Спробуй ще раз:")
    except InvalidOperation:
        return await message.answer(text="Введи, будь ласка, коректне число:")

    return num
