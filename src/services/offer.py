from src.database.models.offer import OfferType
from src.repositories.offer import OfferRepository
from src.repositories.user import UserRepository


class OfferService:
    def __init__(self):
        self.offer_repository = OfferRepository()
        self.user_repository = UserRepository()

    async def create_offer(self, telegram_user_id: int, data: dict):
        creator_id = (await self.user_repository.get_one(telegram_user_id=telegram_user_id)).id
        data["creator_id"] = creator_id
        data["offer_type"] = OfferType(data["offer_type"]).name
        await self.offer_repository.add_one(data=data)
