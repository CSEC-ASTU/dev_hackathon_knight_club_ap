from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .help import bot_help
from .start import bot_start
from .feedback_handler import (
    send_email_feed,
    process_feedback,
    process_feedback_email,
    process_invalid_feedback_email,
    cancel_handler,
    FeedBackForm,
    send_email_feed,
)
from .seminar_handler import (
    send_full_name_seminar,
    process_full_name,
    process_seminar_email,
    process_invalid_seminar_email,
    process_phone_number,
    process_doc,
    cancel_handler,
    SeminarForm,
)

from .registration_handler import (
    send_full_name_reg,
    process_full_name_reg,
    process_id_reg,
    process_invalid_reg_email,
    process_reg_email,
    process_age_invalid_reg,
    process_age_reg,
    process_phone_number_reg,
    RegistrationForm,
)


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_callback_query_handler(
        cancel_handler, lambda call: call.data == "cancel"
    )
    dp.register_callback_query_handler(
        send_email_feed, lambda call: call.data == "send_e_feed"
    )
    dp.register_message_handler(
        process_invalid_feedback_email,
        lambda message: "@" not in message.text,
        state=FeedBackForm.email,
    )
    dp.register_message_handler(process_feedback_email, state=FeedBackForm.email)
    dp.register_message_handler(process_feedback, state=FeedBackForm.feedback)
    # seminar
    dp.register_callback_query_handler(
        send_full_name_seminar, lambda call: call.data == "send_fn_sem"
    )
    dp.register_message_handler(process_full_name, state=SeminarForm.full_name)
    dp.register_message_handler(
        process_invalid_seminar_email,
        lambda message: "@" not in message.text,
        state=SeminarForm.email,
    )
    dp.register_message_handler(process_seminar_email, state=SeminarForm.email)
    dp.register_message_handler(process_phone_number, state=SeminarForm.phone_number)
    dp.register_message_handler(
        process_doc, content_types=types.ContentType.ANY, state=SeminarForm.doc
    )
    # registration
    dp.register_message_handler(
        send_full_name_reg, lambda call: call.data == "send_fn_reg"
    )
    dp.register_message_handler(process_full_name_reg, state=RegistrationForm.full_name)
    dp.register_message_handler(
        process_invalid_reg_email,
        lambda message: "@" not in message.text,
        state=RegistrationForm.email,
    )
    dp.register_message_handler(process_reg_email, state=RegistrationForm.email)
    dp.register_message_handler(
        process_age_invalid_reg,
        lambda message: message.text.isdigit(),
        state=RegistrationForm.age,
    )
    dp.register_message_handler(process_age_reg, state=RegistrationForm.age)
    dp.register_message_handler(
        process_phone_number_reg, state=RegistrationForm.phone_number
    )
    dp.register_message_handler(process_id_reg, state=RegistrationForm.school_id)
