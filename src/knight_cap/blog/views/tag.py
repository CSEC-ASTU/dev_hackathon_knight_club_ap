from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from blog.models import Tag


class AddTagView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tag
    fields = ("name", "description")
    template_name = "blog/tag/add.html"
    permission_required = ("blog.add_tag",)
    success_message = _("Tag '%(name)s' is successfully added!")
    extra_context = {"title": _("Add Tag")}

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateTagView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    fields = ("name", "description")
    template_name = "blog/tag/update.html"
    permission_required = ("blog.change_tag",)
    success_message = _("Tag '%(name)s' is updated successfully!")
    extra_context = {"title": _("Update Tag")}


class ListTagView(PermissionRequiredMixin, ListView):
    model = Tag
    context_object_name = "tags"
    permission_required = ("blog.add_tag", "blog.view_tag")
    extra_context = {"title": _("Tags")}
    template_name = "blog/tag/list.html"


class DeleteTagView(PermissionRequiredMixin, DeleteView):
    model = Tag
    permission_required = ("blog.delete_tag",)
    http_method_names = ["post"]
    success_url = reverse_lazy("blog:list_tag")
