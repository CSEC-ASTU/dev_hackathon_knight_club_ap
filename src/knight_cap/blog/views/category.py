from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from blog.models import Category


class AddCategoryView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ("name", "description")
    template_name = "blog/category/add.html"
    permission_required = ("blog.add_category",)
    success_message = _("Category '%(name)s' is successfully added!")
    extra_context = {"title": _("Add Category")}

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateCategoryView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ("name", "description")
    template_name = "blog/category/update.html"
    permission_required = ("blog.change_category",)
    success_message = _("Category '%(name)s' is updated successfully!")
    extra_context = {"title": _("Update Category")}


class ListCategoryView(PermissionRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    permission_required = ("blog.add_category", "blog.view_category")
    extra_context = {"title": _("Categories")}
    template_name = "blog/category/list.html"


class DeleteCategoryView(PermissionRequiredMixin, DeleteView):
    model = Category
    permission_required = ("blog.delete_category",)
    http_method_names = ["post"]
    success_url = reverse_lazy("blog:list_category")
