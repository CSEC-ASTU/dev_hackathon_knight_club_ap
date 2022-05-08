from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks


async def bot_start(msg: types.Message):
    if position.get_user_position() == "admin":
        pass
    elif position.get_user_position() == "member":
        pass
    elif position.get_user_position() == "guest":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            *[
                types.InlineKeyboardButton(t, callback_data=c)
                for t, c in callbacks.NON_MEMBERS["start"]
            ]
        )
        await msg.reply_photo(
            "https://pbs.twimg.com/profile_images/928609303224881153/FfF79fAl_400x400.jpg",
            caption=hbold("CSEC ASTU"),
            parse_mode="HTML",
            reply_markup=markup,
        )
