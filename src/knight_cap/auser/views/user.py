from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from auser.forms import UserChangeForm
from auser.mixins import CurrentUserMixin

UserModel = get_user_model()


class ProfileEditView(
    PermissionRequiredMixin,
    CurrentUserMixin,
    SuccessMessageMixin,
    UpdateView,
):
    """Generic view used to update user profile"""

    model = UserModel
    form_class = UserChangeForm
    success_url = reverse_lazy("auser:profile_edit")
    permission_required = ("auser.change_user",)
    template_name = "auser/user/profile_edit.html"
    success_message = _("%(first_name)s %(last_name)s profile updated successfully")
    extra_context = {"title": _("Edit Profile")}
