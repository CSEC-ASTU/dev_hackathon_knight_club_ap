from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Text

from .help import bot_help
from .start import bot_start, callback_start


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())

    dp.register_callback_query_handler(
        callback_start, lambda call: call.data == "start"
    )
