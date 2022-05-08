import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext


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
