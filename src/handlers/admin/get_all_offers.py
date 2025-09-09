from aiogram import F, Router
from aiogram.types import Message

from src.constants import constants
from src.services.offer import OfferService


get_all_offers_router = Router()


@get_all_offers_router.message(F.text.lower() == constants.VIEW_OFFERS.lower())
async def get_all_offers_command(message: Message):
    offer_service = OfferService()
    offers = await offer_service.get_all_offers(message.from_user.id)
    print()
    print()
    print()
    print(offers)
    print()
    print()
    print()

    # todo возвращает <src.database.models.offer.Offer object at 0x79db2bf93790> вместо данных?

    # if not offers:
    #     await message.answer(text="Поки що немає доступних оферів.")
    # else:
    #     for offer in offers:
    #         await message.answer(
    #             text=(
    #                 f"🏷️ <b>Назва оферу:</b> {offer.title}\n"
    #                 f"🌐 <b>Тип оферу:</b> {offer.offer_type}\n"
    #                 f"💰 <b>Оплата:</b> {offer.payment}\n"
    #                 f"📄 <b>Опис:</b> {offer.description}\n"
    #                 f"🔗 <b>Посилання:</b> {offer.link}\n"
    #                 f"👤 <b>Контактна особа:</b> {offer.contact_person}\n"
    #                 f"✉️ <b>Email:</b> {offer.email}\n"
    #                 f"📞 <b>Телефон:</b> {offer.phone}\n"
    #             )
    #         )
