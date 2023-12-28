import asyncio
import logging

from aiogram import Dispatcher
from work_tg_bot.database.db import Base, engine

from handlers import core, dns
from work_tg_bot.services.dns import check_dns_loop


async def bot_loop():
    from create_bot import bot
    dp = Dispatcher()

    #Привязка роутеров
    dp.include_router(core.router)
    dp.include_router(dns.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Включаем логирование и инициализируем бд
    logging.basicConfig(level=logging.INFO)
    Base.metadata.create_all(engine)

    # Запуск асинхронных задач
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(check_dns_loop()),
        ioloop.create_task(bot_loop())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
