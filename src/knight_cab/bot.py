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
from handlers.user import guest

from data import config


if __name__ == "__main__":
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())
    user.setup(dp)
    guest.setup(dp)
    executor.start_polling(dp, skip_updates=True)


# # start
# @dp.message_handler(commands=["start"])
# async def start(message: types.Message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     markup.add(
#         *[
#             types.InlineKeyboardButton(t, callback_data=c)
#             for t, c in callbacks.NON_MEMBERS["start"]
#         ]
#     )
#     await message.reply_photo(
#         "https://pbs.twimg.com/profile_images/928609303224881153/FfF79fAl_400x400.jpg",
#         caption=hbold("CSEC ASTU"),
#         parse_mode="HTML",
#         reply_markup=markup,
#     )


# @dp.callback_query_handler(lambda call: call.data == "/start")
# async def start_(call: types.CallbackQuery):
#     await start(call.message)


# # divisions
# @dp.callback_query_handler(lambda call: call.data == "d")
# async def divisions(call: types.CallbackQuery):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in callbacks.NON_MEMBERS["divisions"]])
#     await call.message.edit_reply_markup(reply_markup=markup)


# # division : development
# @dp.callback_query_handler(lambda call: call.data == "dev")
# async def dev(call: types.CallbackQuery):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in callbacks.NON_MEMBERS["development"]])
#     await call.message.delete()
#     await call.message.answer(
#         text=hbold("Development"), reply_markup=markup, parse_mode="HTML"
#     )

# # division : competitive programming
# @dp.callback_query_handler(lambda call: call.data == "cp")
# async def com_pro(call: types.CallbackQuery):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in callbacks.NON_MEMBERS["competitive programming"]])
#     await call.message.delete()
#     await call.message.answer(
#         text=hbold("Competitive Programming"), reply_markup=markup, parse_mode="HTML"
#     )

# # division : capacity building
# @dp.callback_query_handler(lambda call: call.data == "cb")
# async def com_pro(call: types.CallbackQuery):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in callbacks.NON_MEMBERS["capacity building"]])
#     await call.message.delete()
#     await call.message.answer(
#         text=hbold("Capacity Building"), reply_markup=markup, parse_mode="HTML"
#     )

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)

#############################################################################################################################
# # noinspection PyUnusedLocal
# async def on_startup(app: web.Application):
#     import middlewares
#     import filters
#     import handlers
#     middlewares.setup(dp)
#     filters.setup(dp)
#     handlers.errors.setup(dp)
#     handlers.user.setup(dp)
#     # logger.info('Configure Webhook URL to: {url}', url=config.WEBHOOK_URL)
#     # await dp.bot.set_webhook(config.WEBHOOK_URL)


# async def on_shutdown(app: web.Application):
#     app_bot: Bot = app['bot']
#     await app_bot.close()


# async def init() -> web.Application:
#     from utils.misc import logging
#     import web_handlers
#     logging.setup()
#     scheduler = await aiojobs.create_scheduler()
#     app = web.Application()
#     # subapps: List[Tuple[str, web.Application]] = [
#         # ('/tg/webhooks/', web_handlers.tg_updates_app),
#     # ]
#     # for prefix, subapp in subapps:
#     #     subapp['bot'] = bot
#     #     subapp['dp'] = dp
#     #     subapp['scheduler'] = scheduler
#     #     app.add_subapp(prefix, subapp)
#     app.on_startup.append(on_startup)
#     app.on_shutdown.append(on_shutdown)
#     return app


# if __name__ == '__main__':
#     bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
#     storage = RedisStorage2(**config.redis)
#     dp = Dispatcher(bot, storage=storage)

#     web.run_app(init())
