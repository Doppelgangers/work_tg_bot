import logging
import socket
import asyncio
from datetime import datetime
from work_tg_bot.database.db import DNSRecord, Session
from work_tg_bot.utils import send_message_dns


async def check_dns():
    # Открываем сессию с бд
    with Session() as session:
        # Получаем записи с статусом ожидания
        data: list[DNSRecord] = session.query(DNSRecord).filter(DNSRecord.status == "pending").all()

        for record in data:
            #  Проверяем ip из списка на привязку
            this_ip = socket.getaddrinfo(record.domain, 80)[0][-1][0]

            logging.info(f"""Домен: {record.domain}, Ожидаемое ip: {record.host}, Текущий ip: {this_ip}""")

            #  Изменяем статус и отсылаем уведомление
            if this_ip == record.host:
                record.status = "done"
                session.commit()
                await send_message_dns(f"""Домен: {record.domain}\nБыл успешно привязан к {this_ip}""")


async def check_dns_loop():
    while True:
        logging.info(f"{datetime.strftime(datetime.now(), '%H:%M')} - Проверка DNS:")

        try:
            await check_dns()
        except Exception as e:
            logging.error(e)

        await asyncio.sleep(20)
