import asyncio

from aiogram import Bot

from bot_config import bot, dp, database

from handlers.start import start_router
from handlers.dialoge import hw_router


async def on_startup(bot: Bot):
    database.create_tables()




async def main():
    dp.include_router(start_router)
    dp.include_router(hw_router)
    await dp.start_polling()