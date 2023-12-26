from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from work_tg_bot.keyboards.core_kb import get_core_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Выберите действие:", reply_markup=get_core_kb())
