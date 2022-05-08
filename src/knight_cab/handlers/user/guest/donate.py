from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks
from .payment.paypal import pay_with_paypal

async def donating_options(call: types.CallbackQuery):
    options = (
        ("💳 PayPal", "paypal"),
        ("🏦 Bank Transfer", "bank_transfer"),
        ("💸 Bitcoin", "bitcoin"),
        ("📱 Mobile Money", "mobile_money"),
        ("⬅️ Back", "start"),
    )
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*[types.InlineKeyboardButton(t, callback_data=c) for t, c in options])

    await call.message.edit_reply_markup(markup)
    

async def pay_w_paypal(call: types.CallbackQuery):
    transaction = pay_with_paypal(call.data)
    # create a button with a url link to the transaction
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(
        "Pay 1$ with PayPal",
        url=transaction["status_url"],
    )
    markup.add(button)
    await call.message.bot.send_message(call.from_user.id, "Click the link below!", reply_markup=markup)
