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


'''
Тебе нужно открыть папку с установленными пакетами, найти там папки:

    aiogram > bot

Там будут 2 файла - это api.py и base.py.

В base.py найди строку async with session.get(url, timeout=timeout, proxy=self.proxy, proxy_auth=self.proxy_auth) as response и вставь в параметры ssl=False.

А в файле api.py - найди строку async with session.post(url, data=req, **kwargs) as response и аналогичным образом добавь в парамеры ssl=False.

Это все что нужно, но рекомендую использовать этот метод только для локального использования или тестирования как быстрый аппроач, так как это вмешательство в библиотеку. При обновлении либы - все станет как было.


'''

