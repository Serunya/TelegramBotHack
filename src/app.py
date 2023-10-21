import os
import sys
import asyncio
import logging
import commands
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

dp = Dispatcher()
async def start_bot(token):
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    token = os.environ.get('tg_token')
    asyncio.run(start_bot(token))