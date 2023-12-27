import asyncio
import logging

from aiogram import Dispatcher
from work_tg_bot.database.db import Base, engine

from handlers import core, dns
from work_tg_bot.utils import check_dns_loop

logging.basicConfig(level=logging.INFO)


async def bot_loop():
    Base.metadata.create_all(engine)
    from create_bot import bot
    dp = Dispatcher()

    dp.include_routers(core.router, dns.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(check_dns_loop()),
        ioloop.create_task(bot_loop())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
