from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks


async def my_div(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        *[
            types.InlineKeyboardButton(t, callback_data=c)
            for t, c in callbacks.MEMBERS["my_div"]
        ]
    )

    # print(dir(call.message))
    await call.message.edit_reply_markup(
        markup
    )