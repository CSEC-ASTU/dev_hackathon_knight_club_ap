from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks


async def donating_options(call: types.CallbackQuery):
    options = (
        ("💳 PayPal", "paypal"),
        ("🏦 Bank Transfer", "bank_transfer"),
        ("💸 Bitcoin", "bitcoin"),
        ("📱 Mobile Money", "mobile_money"),
    )
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in options])

    await call.message.edit_reply_markup(markup)