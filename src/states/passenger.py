from aiogram.fsm.state import StatesGroup, State


class PassengerStates(StatesGroup):
    NEUTRAL = State()
    AWAITING_TICKET = State()
