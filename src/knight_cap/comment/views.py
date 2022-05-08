from django.apps import apps
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView
from django_comments.models import Comment


class CommentListView(PermissionRequiredMixin, ListView):
    model = Comment
    template_name = "comment/list.html"
    permission_required = ("django_comments.view_comment",)
    context_object_name = "comments"
    extra_context = {"title": _("Comments")}

    def get_object(self, app_name, model_name, pk):
        try:
            model = apps.get_model(app_name, model_name)
            try:
                obj = model.objects.get(pk=pk)
                return obj
            except model.DoesNotExist:
                raise Http404(
                    _("No %(verbose_name)s found matching the query")
                    % {"verbose_name": model._meta.verbose_name}
                )
        except LookupError as error:
            raise Http404("Model not found.")

    def get_queryset(self):
        context_object = self.get_object(
            self.kwargs["app_name"], self.kwargs["model_name"], self.kwargs["pk"]
        )
        return context_object.comments.all()


class MakeCommentPrivateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    fields = ["is_public"]
    permission_required = ("django_comments.change_comment",)
    success_message = _("Comment made private")
    http_method_names = ["post"]

    def form_valid(self, form):
        form.instance.is_public = False
        return super().form_valid(form)

    def get_queryset(self):
        return self.model.objects.filter(is_public=True)

    def get_success_url(self):
        app_name = self.object.content_object._meta.app_label
        model_name = self.object.content_object._meta.model_name
        pk = self.object.content_object.pk
        return reverse_lazy(
            "comment:comment_list",
            kwargs={"app_name": app_name, "model_name": model_name, "pk": pk},
        )


class MakeCommentPublicView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    fields = ["is_public"]
    permission_required = ("django_comments.change_comment",)
    success_message = _("Comment made public")
    http_method_names = ["post"]

    def form_valid(self, form):
        form.instance.is_public = True
        return super().form_valid(form)

    def get_queryset(self):
        return self.model.objects.filter(is_public=False)

    def get_success_url(self):
        app_name = self.object.content_object._meta.app_label
        model_name = self.object.content_object._meta.model_name
        pk = self.object.content_object.pk
        return reverse_lazy(
            "comment:comment_list",
            kwargs={"app_name": app_name, "model_name": model_name, "pk": pk},
        )
