# Головний файл запуску Telegram-бота на aiogram
# Налаштовує логування, підключає роутери, ініціалізує прогрес користувачів

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio
import os

from dotenv import load_dotenv

# Імпортуємо всі хендлери та модуль прогресу
from handlers import start, training, faq, testing
from data import progress

load_dotenv()

print("🔑 API KEY:", os.getenv("OPENROUTER_API_KEY"))  # Для перевірки наявності ключа API

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Токен бота з .env

async def main():
    # Ініціалізація бота та диспетчера
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Підключаємо всі роутери (обробники команд)
    dp.include_router(start.router)
    dp.include_router(training.router)
    dp.include_router(faq.router)
    dp.include_router(testing.router)

    # Завантажуємо прогрес користувачів з файлу
    progress.load_progress()

    # Видаляємо старий webhook та запускаємо polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
