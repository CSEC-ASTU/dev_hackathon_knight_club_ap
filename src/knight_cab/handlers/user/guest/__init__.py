from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
import re

from .feedback_handler import (
    send_email_feed,
    process_feedback,
    process_feedback_email,
    process_invalid_feedback_email,
    cancel_handler,
    send_email_feed,
    FeedBackForm,
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

from .club_exhibit import detail_options

from .donate import donating_options, pay_w_paypal
from .payment.direct_bank import display_bank_details

def setup(dp: Dispatcher):
    dp.register_message_handler(
        cancel_handler, Text(equals="cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(
        process_invalid_feedback_email,
        lambda message: re.match("[^@]+@[^@]+\.[^@]+", message.text) is None,
        state=FeedBackForm.email,
    )
    dp.register_message_handler(
        process_invalid_seminar_email,
        lambda message: re.match("[^@]+@[^@]+\.[^@]+", message.text) is None,
        state=SeminarForm.email,
    )
    dp.register_message_handler(
        process_invalid_reg_email,
        lambda message: re.match("[^@]+@[^@]+\.[^@]+", message.text) is None,
        state=RegistrationForm.email,
    )
    ############################################################################
    dp.register_callback_query_handler(
        send_full_name_reg, lambda call: call.data == "send_fn_reg"
    )
    dp.register_callback_query_handler(
        send_email_feed, lambda call: call.data == "send_e_feed"
    )
    dp.register_callback_query_handler(
        send_full_name_seminar, lambda call: call.data == "send_fn_sem"
    )
    dp.register_callback_query_handler(
        detail_options, lambda call: call.data.startswith("ex_")
    )
    dp.register_callback_query_handler(
        donating_options, lambda call: call.data == "donate"
    )
    dp.register_callback_query_handler(
        pay_w_paypal, lambda call: call.data == "paypal"
    )
    dp.register_callback_query_handler(
        display_bank_details, lambda call: call.data == "bank_transfer"
    )
    ############################################################################
    dp.register_message_handler(process_feedback_email, state=FeedBackForm.email)
    dp.register_message_handler(process_feedback, state=FeedBackForm.feedback)
    # seminar
    dp.register_message_handler(process_full_name, state=SeminarForm.full_name)
    dp.register_message_handler(process_seminar_email, state=SeminarForm.email)
    dp.register_message_handler(process_phone_number, state=SeminarForm.phone_number)
    dp.register_message_handler(
        process_doc, content_types=types.ContentType.ANY, state=SeminarForm.doc
    )
    # registration
    dp.register_message_handler(
        process_age_invalid_reg,
        lambda message: not message.text.isdigit(),
        state=RegistrationForm.age,
    )
    dp.register_message_handler(process_full_name_reg, state=RegistrationForm.full_name)
    dp.register_message_handler(process_reg_email, state=RegistrationForm.email)
    dp.register_message_handler(process_age_reg, state=RegistrationForm.age)
    dp.register_message_handler(
        process_phone_number_reg, state=RegistrationForm.phone_number
    )
    dp.register_message_handler(process_id_reg, state=RegistrationForm.school_id)
