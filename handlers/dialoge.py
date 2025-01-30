from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database

hw_router = Router()

class Homework(StatesGroup):
    name = State()
    number_of_hw = State()
    link = State()

@hw_router.message(Command('SendHw'))
async def send_hw(message: types.Message, state: FSMContext):
    await message.answer('Введите имя')
    await state.set_state(Homework.name)

@hw_router.message(Homework.name)
async def send_hw(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите номер домашки')
    await state.set_state(Homework.number_of_hw)


@hw_router.message(Homework.number_of_hw)
async def send_hw(message: types.Message, state: FSMContext):
    await state.update_data(number_of_hw=message.text)
    await message.answer('Вставьте ссылку')
    await state.set_state(Homework.link)

@hw_router.message(Homework.link)
async def send_hw(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer('Спасибо, дз была успешно отправлена')
    data = state.get_data()
    database.save_hw(data)
    await state.clear()



