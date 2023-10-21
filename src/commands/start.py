from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(PassengerStates.login)
    kb = [
        [
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Добавить билет")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Привет нахуй", reply_markup=keyboard)
