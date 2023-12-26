import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from decouple import config
from handlers import core, dns


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config("BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_routers(core.router, dns.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
