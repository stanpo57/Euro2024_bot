import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.handlers import router

from config import BOT_TOKEN


async def main():
    # print(BOT_TOKEN)
    bot = Bot(token=BOT_TOKEN)  # stanpo1586_bot
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off!")
