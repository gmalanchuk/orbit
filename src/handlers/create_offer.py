from decimal import Decimal

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.constants import constants
from src.handlers.validators.create_offer import (
    name_validator,
    offer_type_validator,
    price_per_subscriber_validator,
    telegram_channel_url_validator,
)
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
    await message.answer(text="Придумай назву своєму оферу:", reply_markup=main_menu_keyboard)
    await state.set_state(CreateProfileStates.name)


@create_offer_router.message(CreateProfileStates.name)
async def state_name(message: Message, state: FSMContext):
    validator = await name_validator(message)
    if validator:
        return

    print()
    print(message.text)  # todo проверить че происходит когда нажимаешь кнопку головне меню
    print()

    await state.update_data(name=message.text)
    await message.answer(text="Введи посилання на телеграм канал:", reply_markup=main_menu_keyboard)
    await state.set_state(CreateProfileStates.telegram_channel_url)


@create_offer_router.message(CreateProfileStates.telegram_channel_url)
async def state_telegram_channel_url(message: Message, state: FSMContext):
    validator = await telegram_channel_url_validator(message)
    if validator:
        return

    await state.update_data(telegram_channel_url=message.text)
    await message.answer(text="Вибери тип оферу із нижче запропонованих:", reply_markup=offer_type_keyboard)
    await state.set_state(CreateProfileStates.offer_type)


@create_offer_router.message(CreateProfileStates.offer_type)
async def state_offer_type(message: Message, state: FSMContext):
    validator = await offer_type_validator(message)
    if validator:
        return

    await state.update_data(offer_type=message.text)
    await message.answer(text="Введи плату, яку отримає трафер за одного підписника:", reply_markup=main_menu_keyboard)
    await state.set_state(CreateProfileStates.price_per_subscriber)


@create_offer_router.message(CreateProfileStates.price_per_subscriber)
async def state_price_per_subscriber(message: Message, state: FSMContext):
    num = await price_per_subscriber_validator(message)
    if type(num) is not Decimal:
        return

    await state.update_data(price_per_subscriber=num)

    user_data = await state.get_data()
    await OfferService().create_offer(telegram_user_id=message.from_user.id, data=user_data)

    await message.answer(
        text="Офер було успішно створено! Зміни статус офера в налаштуваннях, щоб запустити його."
    )  # todo здесь в тексте вставить ссылку на настройки офера
    await state.clear()
