from aiogram import types

from utils.misc import rate_limit


@rate_limit(5, "help")
async def bot_help(msg: types.Message):
    text = ["Help Section: ", "/start - Main Menu", "/help - Help Section"]
    await msg.answer("\n".join(text))
