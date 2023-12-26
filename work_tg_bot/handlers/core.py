from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from sqlite import Session, DNSRecord
from work_tg_bot.handlers import validators
from work_tg_bot.keyboards.core_kb import get_core_kb

router = Router()


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer("Выберите действие:", reply_markup=get_core_kb())


@router.message(Command("waitdns"))
async def waitdns(message: Message):
    args = message.text.split()
    if len(args) != 3:
        await message.answer("Неверный формат команды. Используйте /waitdns <домен> <ip>")
        return

    domain: str = args[1].strip()
    wait_ip: str = args[2].strip()

    if not validators.check_domain_name(domain):
        await message.reply("Некорректный домен.")
        return
    if not validators.check_ip_address(wait_ip):
        await message.reply("Некорректный IP адрес.")
        return

    session = Session()

    record = DNSRecord(domain=domain, host=wait_ip, user_id= message.from_user.id)

    session.add(record)

    session.commit()

    await message.answer(f"Зарезервировано {wait_ip} в домен {domain}")
