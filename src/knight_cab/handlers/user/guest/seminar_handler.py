import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from data import seminar_data


logging.basicConfig(level=logging.INFO)


# state


class SeminarForm(StatesGroup):
    full_name = State()
    email = State()
    phone_number = State()
    doc = State()


# handlers
async def send_full_name_seminar(msg: types.Message):
    """
    Entry point for Seminar Request state
    """
    await SeminarForm.full_name.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
    await msg.bot.send_message(
        msg.from_user.id,
        "<b>Request for Seminar</b>:\n\nFull Name:",
        reply_markup=markup,
    )


async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.bot.send_message(
        message.from_user.id, "Cancelled.", reply_markup=types.ReplyKeyboardRemove()
    )


async def process_full_name(message: types.Message, state: FSMContext):
    """
    Process full name
    """

    await state.update_data(full_name=message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))

    await message.bot.send_message(
        message.from_user.id, "Send us your email:", reply_markup=markup
    )
    await SeminarForm.next()


async def process_invalid_seminar_email(msg: types.Message):
    # print(msg.text)
    return await msg.bot.send_message(msg.from_user.id, "Invalid Email!")


async def process_seminar_email(message: types.Message, state: FSMContext):
    """
    Proccess user email and assign it to the current state
    """
    async with state.proxy() as data:
        data["email"] = message.text
        await SeminarForm.next()
        await state.update_data(email=message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
        await message.bot.send_message(
            message.from_user.id, "Phone Number:", reply_markup=markup
        )


async def process_phone_number(msg: types.Message, state: FSMContext):
    """
    Process phone number
    """
    async with state.proxy() as data:
        data["phone_number"] = msg.text
    await SeminarForm.next()
    await state.update_data(email=msg.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
    await msg.bot.send_message(
        msg.from_user.id, "Presentation Slide:", reply_markup=markup
    )


async def process_doc(msg: types.File, state: FSMContext):
    """
    Process document
    """
    async with state.proxy() as data:
        data["slide"] = msg.file_id
    try:
        seminar_data.send_seminar(
            data["token"],
            data["full_name"],
            data["email"],
            data["phone_number"],
            data["slide"],
        )
    except:
        logging.error("Error sending seminar request!")

    await msg.bot.send_message(
        msg.from_user.id, "Thank you for reaching out, your request is being processed!"
    )
    print(data)
    # Finish conversation
    await state.finish()
