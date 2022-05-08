import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from data import seminar_data


logging.basicConfig(level=logging.INFO)


# state


class RegistrationForm(StatesGroup):
    full_name = State()
    school_id = State()
    email = State()
    age = State()
    phone_number = State()


# handlers
async def send_full_name_reg(msg: types.Message):
    """
    Entry point for Seminar Request state
    """
    await RegistrationForm.full_name.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))

    await msg.bot.send_message(
        msg.from_user.id,
        "<b>Registration</b>\n\nFull Name:",
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


async def process_full_name_reg(message: types.Message, state: FSMContext):
    """
    Process full name
    """

    await state.update_data(full_name=message.text)
    await RegistrationForm.next()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))

    await message.bot.send_message(
        message.from_user.id, "Send us your ID:", reply_markup=markup
    )


async def process_id_reg(message: types.Message, state: FSMContext):
    """
    Process School ID
    """

    await state.update_data(school_id=message.text.upper())
    await RegistrationForm.next()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))

    await message.bot.send_message(
        message.from_user.id, "Send us your email:", reply_markup=markup
    )


async def process_invalid_reg_email(msg: types.Message):
    return await msg.bot.send_message(msg.from_user.id, "Invalid Email!")


async def process_reg_email(message: types.Message, state: FSMContext):
    """
    Proccess user email and assign it to the current state
    """
    async with state.proxy() as data:
        data["email"] = message.text
        await RegistrationForm.next()
        await state.update_data(email=message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
        await message.bot.send_message(
            message.from_user.id, "Age:", reply_markup=markup
        )


async def process_age_invalid_reg(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


async def process_age_reg(message: types.Message, state: FSMContext):
    """
    Process age
    """
    # Update state and data
    await RegistrationForm.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))

    await message.bot.send_message(
        message.from_user.id, "What is your phone number?", reply_markup=markup
    )


async def process_phone_number_reg(msg: types.Message, state: FSMContext):
    """
    Process phone number
    """
    async with state.proxy() as data:
        data["phone_number"] = msg.text
    await RegistrationForm.next()
    await state.update_data(email=msg.text)

    await msg.bot.send_message(
        msg.from_user.id,
        "Registration complete!",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    print(data)
    # Finish conversation
    await state.finish()
