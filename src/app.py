import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


token = os.environ.get('6933743208:AAG1ZMc4ozQJic9zZ7l5pSMnm2tyvSFqtyc')

dp = Dispatcher()


def start_bot(token):
    pass


if token:
    start_bot(token)
else:
    sys.stderr.write("token not found")


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


async def main():
    bot = Bot('6933743208:AAG1ZMc4ozQJic9zZ7l5pSMnm2tyvSFqtyc')
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
