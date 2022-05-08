from data import auth
from aiogram import types


def get_user_info():
    user_data = {
        "name": "test",
        "username": "test",
        "first_name": "test",
        "last_name": "test",
        "position": "admin",
    }
    return user_data


def get_user_position():
    data = get_user_info()
    return data["position"]
