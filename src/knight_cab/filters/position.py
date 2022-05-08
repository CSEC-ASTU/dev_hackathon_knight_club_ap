from data import auth
from aiogram import types
import requests


def get_user_info():
    user_data = {
        "name": "test",
        "username": "test",
        "first_name": "test",
        "last_name": "test",
        "position": "guest",
    }
    return user_data


def get_user_position():
    data = get_user_info()
    return data["position"]
