import sys
import asyncio
import logging
import commands
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from commands.start import start_router
from commands.get_user_information import information_router
from commands.add_ticket import add_ticket_router


# token = os.environ.get('tg_token')
token = "6933743208:AAG1ZMc4ozQJic9zZ7l5pSMnm2tyvSFqtyc"
bot = Bot(token, parse_mode=ParseMode.HTML)


async def main() -> None:
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        information_router,
        add_ticket_router,
    )

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
