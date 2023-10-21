import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher
import commands
from aiogram.filters import CommandStart

dp = Dispatcher()
async def start_bot(token):
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    token = "dsa"
    asyncio.run(start_bot(token))