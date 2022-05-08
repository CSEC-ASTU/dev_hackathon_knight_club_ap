from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)
from django_filters.views import FilterView

from blog.filters import PostFilter
from blog.forms import AddPostForm, UpdatePostForm
from blog.models import Category, Post, Tag


class AddPostView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """A view for creating new posts."""

    model = Post
    form_class = AddPostForm
    template_name = "blog/post/add.html"
    success_url = reverse_lazy("blog:list_post_admin")
    permission_required = ("blog.add_post",)
    success_message = _("Post '%(title)s' is successfully added!")
    extra_context = {"title": _("Add Blog")}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author_id = self.request.user.id
        self.object.save()
        return super().form_valid(form)


class UpdatePostView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """A generic view for updating existing posts."""

    model = Post
    form_class = UpdatePostForm
    template_name = "blog/post/update.html"
    permission_required = ("blog.change_post",)
    success_message = _("Post '%(title)s' is updated successfully!")
    extra_context = {"title": _("Update Blog")}


class LikePostView(PermissionRequiredMixin, View):
    """A generic view for apply like on post."""

    permission_required = ("blog.like_post",)

    def get(self, request, *args, **kwargs):
        post_ = get_object_or_404(Post, id=kwargs["pk"])
        if post_.likes.filter(id=request.user.id).exists():
            post_.likes.remove(request.user)
        else:
            post_.likes.add(request.user)
        return HttpResponseRedirect(reverse_lazy("blog:post_detail", args=[post_.slug]))

    def get_queryset(self):
        return self.model.objects.filter(is_draft=True)


class ListPostView(ListView):
    """A generic view for listing posts for anonymous users."""

    model = Post
    template_name = "blog/post/list.html"
    context_object_name = "posts"
    extra_context = {"title": _("List Blog")}

    def get_queryset(self):
        return self.model.objects.filter(is_draft=True)


class ListPostAdminView(PermissionRequiredMixin, ListView):
    """A generic view for listing posts on admin pages."""

    model = Post
    template_name = "blog/post/list_admin.html"
    permission_required = ("blog.view_post", "blog.add_post")
    context_object_name = "posts"
    extra_context = {"title": _("Blog List")}

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                "model_name": self.model.__name__.lower(),
                "categories": Category.objects.all(),
                "tags": Tag.objects.all(),
            }
        )
        return super().get_context_data(**kwargs)


class PostDetailView(DetailView):
    """A generic view for displaying post detail."""

    model = Post
    template_name = "blog/post/detail.html"

    def get_context_data(self, **kwargs):
        kwargs.update({"title": self.object.title})
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(is_draft=True)


class DeletePostView(PermissionRequiredMixin, DeleteView):
    """A generic view for deleting posts."""

    model = Post
    success_url = reverse_lazy("blog:post_list")
    permission_required = "blog.delete_post"
    http_method_names = ["post"]


class FilterPostView(FilterView):
    filterset_class = PostFilter
    template_name = "blog/post/filter.html"
    extra_context = {"title": _("Filter Blog")}


#
# class CommentListView(PermissionRequiredMixin, DetailView):
#    model = Post
#    template_name = "blog/comment/list.html"
#    permission_required = ('django_comments.view_comment',)
#    extra_context = {'title': _('Comments')}
