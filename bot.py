from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(os.environ["token"])
dp = Dispatcher(bot)

