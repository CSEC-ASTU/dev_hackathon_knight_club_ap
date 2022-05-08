"""auser club entity managements views

	Created by: Wendirad Demelash
	Last modified by: Wendirad Demelash
"""
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from auser.models import Club
from auser.utils import generate_username


class ListActiveClubsView(PermissionRequiredMixin, ListView):
    """Generic view used to list all active clubs."""

    model = Club
    permission_required = ("auser.view_club", "auser.add_club")
    template_name = "auser/club/list_active.html"
    context_object_name = "clubs"
    extra_context = {"title": _("Active clubs")}

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class ListDeactivatedClubsView(PermissionRequiredMixin, ListView):
    """Generic view used to list all deactivated clubs."""

    model = Club
    permission_required = ("auser.view_club", "auser.add_club")
    template_name = "auser/club/list_active.html"
    context_object_name = "clubs"
    extra_context = {"title": _("Active clubs")}

    def get_queryset(self):
        return self.model.objects.filter(is_active=False)


class ClubCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Generic view used to create a new club."""

    model = Club
    fields = (
        "name",
        "username",
        "sex",
        "email",
        "phone_number",
    )
    permission_required = ("auser.add_club",)
    success_message = "Club '%(short_name)s is successfully created"
    template_name = "auser/club/add.html"
    extra_context = {"title": _("Add club")}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = generate_username()
        self.object.save()
        return super().form_valid(form)


class ActivateClubView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """Generic view used to activate a club."""

    model = Club
    fields = ("is_active",)
    permission_required = ("auser.activate_club",)
    success_url = reverse_lazy("auser:active_content_creator_list")
    success_message = _("%(short_name)s activated successfully")
    http_method_names = ["post"]

    def form_valid(self, form):
        form.cleaned_data.update(
            {
                "short_name": self.object.short_name,
            }
        )
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_data = form_kwargs.get("data", {}).copy()
        form_data.update({"is_active": True})
        form_kwargs.update({"data": form_data})
        return form_kwargs

    def get_queryset(self):
        return self.model.objects.filter(is_active=False)


class DeactivateClubView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """Generic view used to deactivate a club."""

    model = Club
    fields = ("is_active",)
    permission_required = ("auser.deactivate_club",)
    success_url = reverse_lazy("auser:active_content_creator_list")
    success_message = _("%(short_name)s deactivated successfully")
    http_method_names = ["post"]

    def form_valid(self, form):
        form.cleaned_data.update(
            {
                "short_name": self.object.short_name,
            }
        )
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_data = form_kwargs.get("data", {}).copy()
        form_data.update({"is_active": False})
        form_kwargs.update({"data": form_data})
        return form_kwargs

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class UpdateClubView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """Generic view used to update a club."""

    model = Club
    fields = (
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
    permission_required = ("auser.change_club",)
    success_url = reverse_lazy("auser:active_content_creator_list")
    template_name = "auser/club/update.html"
    success_message = _("%(first_name)s %(last_name)s updated successfully")
    extra_context = {"title": _("Update club")}

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class ClubDetailView(PermissionRequiredMixin, DetailView):
    """Generic view used to display club details"""

    model = Club
    template_name = "auser/club/detail.html"
    extra_context = {"title": _("Club")}
    permission_required = ("auser.view_club", "auser.add_club")
    context_object_name = "club"


class DeleteClubView(PermissionRequiredMixin, DeleteView):
    """Generic view used to delete club."""

    model = Club
    permission_required = ("auser.delete_club",)
    success_url = reverse_lazy("auser:deactivated_content_creator_list")
    http_method_names = ["post"]

    def get_queryset(self):
        return self.model.objects.filter(is_active=False)
