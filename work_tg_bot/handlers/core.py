from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from work_tg_bot.keyboards.core_kb import get_core_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    await bot.send_message(-4040488512, "qwe")
    await message.answer("Выберите действие:", reply_markup=get_core_kb())


@router.message(Command("clear"))
async def cmd_start(message: Message):
    await message.answer("Отчищено", reply_markup=ReplyKeyboardRemove())

