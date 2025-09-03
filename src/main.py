import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from src.config import settings
from src.handlers.admin import admin_router
from src.handlers.buyer import buyer_router
from src.handlers.main_menu import main_menu_router
from src.handlers.start import start_router


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(start_router, buyer_router, admin_router, main_menu_router)
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
