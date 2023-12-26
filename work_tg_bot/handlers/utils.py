import logging
import socket
import asyncio
from work_tg_bot.database.db import DNSRecord, Session
from work_tg_bot.create_bot import bot

logging.basicConfig(level=logging.INFO)


async def check_dns_loop():
    while True:
        logging.info("check_dns_loop")

        with Session() as session:
            data = session.query(DNSRecord).filter(DNSRecord.status == "pending").all()

            for record in data:
                if socket.getaddrinfo(record.domain, 80)[0][-1][0] == record.host:
                    record.status = "done"
                    session.commit()
                    await bot.send_message(chat_id=record.user_id, text=f"Привязалось {record.domain}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(check_dns_loop())


