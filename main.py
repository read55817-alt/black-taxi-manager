import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🚖 Black Taxi Manager запускается...")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
