import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='6561724098:AAG4PShVBvtFEkz1_yw30iAJJgbnApWGT6M')  # stanpo1586_bot
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off!")

