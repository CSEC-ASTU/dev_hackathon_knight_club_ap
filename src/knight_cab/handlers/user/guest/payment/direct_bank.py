from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks


async def display_bank_details(call: types.CallbackQuery):
    text = "You can support us via our Various Bank Accounts<b>\n\n\nName : CSEC-ASTU \n\nNib Bank Account: 100023453323454324354\n\nCBE Bank Account: 100023453323454324354\n\nDashin Bank Account: 100023453323454324354</b>"
    await call.message.bot.send_message(call.from_user.id, text, parse_mode="HTML")
