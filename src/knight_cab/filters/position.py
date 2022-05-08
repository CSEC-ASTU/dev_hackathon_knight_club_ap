from data import auth
from aiogram import types


def get_user_info():
    user_data = {
        "name": "bura",
        "username": "bura",
        "first_name": "bura",
        "last_name": "bura",
        "position": "guest",
    }
    return user_data


def get_user_position():
    data = get_user_info()
    return data["position"]
