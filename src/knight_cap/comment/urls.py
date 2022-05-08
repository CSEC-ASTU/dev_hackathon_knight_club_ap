from django.urls import re_path

from comment import views

app_name = "comment"

urlpatterns = [
    re_path(
        r"^(?P<app_name>[a-zA-Z_]+)/(?P<model_name>[a-zA-Z_]+)/(?P<pk>\d+)/$",
        views.CommentListView.as_view(),
        name="comment_list",
    ),
    re_path(
        r"^make_private/(?P<pk>\d+)/$",
        views.MakeCommentPrivateView.as_view(),
        name="make_private",
    ),
    re_path(
        r"^make_public/(?P<pk>\d+)/$",
        views.MakeCommentPublicView.as_view(),
        name="make_public",
    ),
]
