from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks


async def detail_options(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        *[
            types.InlineKeyboardButton(t, callback_data=c)
            for t, c in callbacks.NON_MEMBERS[call.data.split("_")[1]]
        ]
    )

    # print(dir(call.message))
    await call.message.edit_reply_markup(
        markup
    )  # f"<b>{call.data.split('_')[1]}</b>", reply_markup=markup)
