from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data import config


def check(message: types.Message):
    return message.from_user.id in config.members