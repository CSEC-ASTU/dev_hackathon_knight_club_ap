from typing import List, Tuple

import aiojobs as aiojobs
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from aiogram.types import ParseMode

# from aiohttp import web
from loguru import logger
from keyboards.inline import callbacks
from handlers import user

from data import config


if __name__ == "__main__":
    bot = Bot(
        token=config.BOT_TOKEN, parse_mode=ParseMode.HTML
    , storage=MemoryStorage())
    dp = Dispatcher(bot)
    user.setup(dp)
    executor.start_polling(dp, skip_updates=True)
    logger.info("Bot started")
    