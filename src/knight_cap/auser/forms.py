from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

UserModel = get_user_model()


class UserChangeForm(forms.ModelForm):
    """Model form used to update user profile"""

    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "sex",
            "location",
            "po_box",
            "profile_picture",
            "bio",
        )
        field_classes = {"username": UsernameField}
