import asyncio
import logging

from aiogram import Dispatcher
from work_tg_bot.database.db import Base, engine

from handlers import core, dns

logging.basicConfig(level=logging.INFO)


async def main():

    Base.metadata.create_all(engine)
    from create_bot import bot
    dp = Dispatcher()

    dp.include_routers(core.router, dns.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
