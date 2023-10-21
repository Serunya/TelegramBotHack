from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.states.passenger import PassengerStates

add_ticket_router = Router()


@add_ticket_router.message(F.text == 'Добавить билет')
async def add_ticket(message: Message, state: FSMContext) -> None:
    await state.set_state(PassengerStates.AWAITING_TICKET)
    await message.answer("Загрузите ваш билет в виде ФОТО или PDF-файла")


@add_ticket_router.message(F.photo, PassengerStates.AWAITING_TICKET)
async def handle_ticket(message: Message, state: FSMContext):
    file_id = message.document.file_unique_id

    await message.answer(file_id)

    await message.answer("Билет успешно загружен и сохранен!")
    await state.clear()

