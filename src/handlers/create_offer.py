from decimal import Decimal, InvalidOperation

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.constants import constants
from src.database.models.offer import OfferType
from src.keyboards.main_menu import main_menu_keyboard
from src.keyboards.offer_type import offer_type_keyboard
from src.services.offer import OfferService


create_offer_router = Router()


class CreateProfileStates(StatesGroup):
    name = State()
    # description = State()
    telegram_channel_url = State()
    offer_type = State()
    # offer_status = State()
    price_per_subscriber = State()

    # user_data = {
    #     "name": 'test',
    #     "telegram_channel_url": 'test',
    #     "price_per_subscriber": 1.5,
    #     "type": OfferType.VACANCIES,
    # }


@create_offer_router.message(F.text.lower() == constants.CREATE_OFFER.lower())
async def create_offer_command(message: Message, state: FSMContext):
    await message.answer(text="Введіть назву оферу:", reply_markup=main_menu_keyboard)  # todo переписать текст
    await state.set_state(CreateProfileStates.name)


@create_offer_router.message(CreateProfileStates.name)
async def state_name(message: Message, state: FSMContext):

    # todo перенести куда-то валидатор
    if len(message.text) > 64:
        return await message.answer(text="Назва оферу не може бути довшою за 64 символи. Введіть назву оферу:")

    print()
    print(message.text)  # todo проверить че происходит когда нажимаешь кнопку головне меню
    print()

    await state.update_data(name=message.text)
    await message.answer(text="Введіть посилання на телеграм канал:", reply_markup=main_menu_keyboard)
    await state.set_state(CreateProfileStates.telegram_channel_url)


@create_offer_router.message(CreateProfileStates.telegram_channel_url)
async def state_telegram_channel_url(message: Message, state: FSMContext):

    # todo перенести куда-то валидатор
    if "t.me/" not in message.text:
        return await message.answer(text="Невірне посилання")  # todo переписать текст ошибки

    await state.update_data(telegram_channel_url=message.text)
    await message.answer(text="Виберіть тип вашого оферу:", reply_markup=offer_type_keyboard)  # todo переписать текст
    await state.set_state(CreateProfileStates.offer_type)


@create_offer_router.message(CreateProfileStates.offer_type)
async def state_offer_type(message: Message, state: FSMContext):

    # todo перенести куда-то валидатор
    types = [e.value for e in OfferType]
    if message.text not in types:
        return await message.answer(
            text="Будь-ласка вибіреть тип оферу з нижче запропонованих:", reply_markup=offer_type_keyboard
        )  # todo переписать текст ошибки

    await state.update_data(offer_type=message.text)
    await message.answer(
        text="Введіть плату за одного підписника:", reply_markup=main_menu_keyboard
    )  # todo переписать текст
    await state.set_state(CreateProfileStates.price_per_subscriber)


@create_offer_router.message(CreateProfileStates.price_per_subscriber)
async def state_price_per_subscriber(message: Message, state: FSMContext):

    # todo перенести куда-то валидатор
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

    await state.update_data(price_per_subscriber=num)

    offer_service = OfferService()
    user_data = await state.get_data()
    await offer_service.create_offer(telegram_user_id=message.from_user.id, data=user_data)

    await message.answer(
        text="Ваш офер було створено, зайдіть в налаштування, щоб його запустити"
    )  # todo переписать текст
    await state.clear()
