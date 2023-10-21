import os
import sys
<<<<<<< HEAD
import asyncio
import logging
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
=======
def start_bot(token):
    pass


token = os.environ.get('tg_token')

if token:
    start_bot(token)
else:
    sys.stderr.write("token not found")
>>>>>>> main
