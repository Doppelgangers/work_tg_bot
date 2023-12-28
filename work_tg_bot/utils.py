import logging
import socket
import asyncio
from datetime import datetime

from work_tg_bot.database.db import DNSRecord, Session
from work_tg_bot.create_bot import bot

logging.basicConfig(level=logging.INFO)


async def check_dns_loop():
    while True:
        try:
            logging.info(f"{datetime.strftime(datetime.now(), '%H:%M:%S')} - Checking DNS:")
            with Session() as session:
                data = session.query(DNSRecord).filter(DNSRecord.status == "pending").all()

                for record in data:
                    this_ip = socket.getaddrinfo(record.domain, 80)[0][-1][0]
                    logging.info(f"check ({record.domain}, {record.host}, {this_ip})")

                    if this_ip == record.host:
                        record.status = "done"
                        session.commit()

                        await bot.send_message(chat_id="-4040488512", text=f"Привязалось {record.domain}")
                await asyncio.sleep(20)
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    asyncio.run(check_dns_loop())


