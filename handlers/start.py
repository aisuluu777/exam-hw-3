from aiogram import types, Router
from aiogram.filters import Command

start_router =  Router()

@start_router.message(Command('start'))
async def start_bot(message: types.Message):
    await message.answer('Привет')
    