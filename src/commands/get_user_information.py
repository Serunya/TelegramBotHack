from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message

information_router = Router()


@information_router.message(F.text == 'Информация')
async def get_information(message: Message) -> None:
    now = datetime.now()
    user_data = {'first_name': 'Генидий',
                 'second_name': 'Альбертович',
                 'last_name': 'Штольц',
                 'ticket_number': '3928179',
                 'dep_city': 'Ростов-на-Дону',
                 'arr_city': 'Пенза',
                 'dep_time': now,
                 'arr_time': now}

    await message.answer(
        f"Информация о пассажире:\n"
        f"ФИО: {user_data['first_name']} {user_data['second_name']} {user_data['last_name']}\n"
        f"Номер билета: {user_data['ticket_number']}\n\n"
        f"Детали отправления:\n"
        f"  {user_data['dep_city']}\n"
        f"  {user_data['dep_time'].strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"Детали прибытия:\n"
        f"  {user_data['arr_city']}\n"
        f"  {user_data['arr_time'].strftime('%Y-%m-%d %H:%M:%S')}"
    )
