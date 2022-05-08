import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import bold, hbold, hitalic, hcode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from data import feedback_data

logging.basicConfig(level=logging.INFO)

# state


class FeedBackForm(StatesGroup):
    email = State()
    feedback = State()


# handlers
async def send_email_feed(msg: types.Message):
    """
    Entry point for feedback state
    """
    await FeedBackForm.email.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
    await msg.bot.send_message(
        msg.from_user.id,
        "<b>Send us a feedback</b>:\n\nEnter your email:",
        reply_markup=markup,
    )


async def process_invalid_feedback_email(msg: types.Message):
    return await msg.bot.send_message("Invalid Email!")


async def process_feedback_email(message: types.Message, state: FSMContext):
    """
    Proccess user email and assign it to the current state
    """
    async with state.proxy() as data:
        data["email"] = message.text
        await FeedBackForm.next()
        await state.update_data(email=message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Cancel", callback_data="cancel"))
        await message.bot.send_message(
            message.from_user.id, "What do you want to tell us?", reply_markup=markup
        )


async def process_feedback(msg: types.Message, state: FSMContext):
    # await FeedBackForm.feedback.set()
    async with state.proxy() as data:
        data["feedback"] = msg.text
    try:
        feedback_data.send_feedback(data["token"], data["email"], data["feedback"])
    except:
        logging.error("Error sending feedback")
    await msg.bot.send_message(
        msg.from_user.id,
        "Thank you for your feedback!",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    # Finish conversation
    await state.finish()


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
