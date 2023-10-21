from aiogram.filters import CommandStart
from aiogram.types import Message
from src.app import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Ne hello, {message.from_user.full_name}!")