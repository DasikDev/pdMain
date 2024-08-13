import asyncio
import logging

from aiogram import Bot, Dispatcher


from handlers import (
    user_handlers,
)


async def bot_start_engine():
    bot = Bot(token="BOT_TOKEN", parse_mode="HTML")

    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(bot_start_engine())
