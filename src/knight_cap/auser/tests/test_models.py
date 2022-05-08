"""
	Tests of ORM of authentication and authorization.

	Created By: Wendirad Demelash
	Last Modified By: Wendirad Demelash
"""
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase

from auser.models import Address


class TestAddressLabels(SimpleTestCase):
    """
    Tests of existing attributes label of Abstract class `Address`.
    """

    def test_email_label(self):
        """test email address field label"""
        email_label = Address._meta.get_field("email").verbose_name
        self.assertEqual(email_label, "email")

    def tests_phone_number_label(self):
        """test phone number field label"""
        phone_number_label = Address._meta.get_field("phone_number").verbose_name
        self.assertEqual(phone_number_label, "phone number")

    def test_pobox_label(self):
        """test P.O.Box field label"""
        po_box_label = Address._meta.get_field("po_box").verbose_name
        self.assertEqual(po_box_label, "P.O Box")


class TestUserLabels(SimpleTestCase):
    """
    Tests of existing attributes label of custom User model
    """

    def setUp(self):
        self.UserModel = get_user_model()

    def test_username_label(self):
        """test user username field label"""
        username_label = self.UserModel._meta.get_field("username").verbose_name
        self.assertEqual(username_label, "username")

    def test_is_active_label(self):
        """test user is_active field label"""
        is_active_label = self.UserModel._meta.get_field("is_active").verbose_name
        self.assertEqual(is_active_label, "active")

    def test_is_staff_label(self):
        """test user is_staff field label"""
        is_staff_label = self.UserModel._meta.get_field("is_staff").verbose_name
        self.assertEqual(is_staff_label, "staff status")
