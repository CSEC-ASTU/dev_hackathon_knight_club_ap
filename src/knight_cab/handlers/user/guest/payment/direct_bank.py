from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from filters import position
from keyboards.inline import callbacks



async def display_bank_details(call: types.CallbackQuery):
    text = "<b>You can donate to our CBE account:</b>\n <i>1000213242354352343</i> \n"
    await call.message.edit_text(text, parse_mode="HTML")