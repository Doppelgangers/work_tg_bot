from decouple import config
from aiogram import Bot
bot = Bot(token=config("BOT_TOKEN"))
