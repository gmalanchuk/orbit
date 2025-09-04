from src.repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, telegram_user_id: int):
        await self.user_repository.add_one(data={"telegram_user_id": telegram_user_id})

    async def get_user(self, telegram_user_id: int):
        return await self.user_repository.get_one(telegram_user_id=telegram_user_id)
