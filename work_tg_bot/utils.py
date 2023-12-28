from decouple import config
from work_tg_bot.create_bot import bot


async def send_message_dns(message: str) -> None:
    chat_id = config("DNS_CHAT_ID")
    await bot.send_message(chat_id=chat_id, text=message)
