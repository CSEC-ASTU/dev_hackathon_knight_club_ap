from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from auser.mixins import ClubRequiredMixin
from auser.models import Club, Division


class DivisionCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Generic view used to create a new club."""

    model = Division
    fields = (
        "name",
        "short_name",
        "logo",
        "description",
        "members_permissions",
        "head_permissions",
    )
    permission_required = ("auser.add_division",)
    success_message = "Division '%(short_name)s is successfully created."
    template_name = "auser/division/add.html"
    extra_context = {"title": _("Add division")}

    def get_success_url(self):
        return reverse_lazy("auser:division_detail", kwargs={"slug": self.object.slug})

    def get_division(self):
        division_pk = self.kwargs.get("division_slug", None)
        if division_pk:
            return Division.objects.get(slug=division_pk)
        return None

    def get_club(self):
        club_name = self.kwargs.get("club_name", None)
        if club_name is not None:
            return Club.objects.get(slug=club_name)
        division = self.get_division()
        if division is not None:
            return division.club
        raise Http404()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.club = self.get_club()
        self.object.parent = self.get_division()
        self.object.save()
        return super().form_valid(form)


class DivisionDetailView(PermissionRequiredMixin, ClubRequiredMixin, DetailView):
    model = Division
    permission_required = ("auser.view_division",)
    template_name = "auser/division/detail.html"
    extra_context = {"title": _("Division")}


class DivisionUpdateView(
    PermissionRequiredMixin, ClubRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Division
    fields = (
        "name",
        "short_name",
        "logo",
        "description",
        "members_permissions",
        "head_permissions",
    )
    permission_required = ("auser.change_division",)
    success_message = "Division '%(short_name)s is successfully updated."
    template_name = "auser/division/update.html"
    extra_context = {"title": _("Update division")}

    def get_success_url(self):
        return reverse_lazy("auser:division_detail", kwargs={"slug": self.object.slug})


class DeleteDivisionView(PermissionRequiredMixin, DeleteView):
    """Generic view used to delete club."""

    model = Division
    permission_required = ("auser.delete_divisoin",)
    http_method_names = ["post"]

    def delete(self, *args, **kwargs):
        division = self.get_object()
        if division.parent:
            self.success_url = reverse_lazy(
                "auser:division_detail", kwargs={"slug": division.parent.slug}
            )
        else:
            self.success_url = reverse_lazy(
                "auser:club_detail", kwargs={"slug": division.club.slug}
            )
        return super().delete(*args, **kwargs)
