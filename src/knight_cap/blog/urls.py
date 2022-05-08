from django.urls import include, re_path
from django.views.decorators.cache import never_cache

from blog import views

app_name = "blog"

post_urlpatterns = [
    re_path(r"^$", views.ListPostView.as_view(), name="list_post"),
    re_path(r"^add/$", views.AddPostView.as_view(), name="add_post"),
    re_path(r"^list/$", views.ListPostAdminView.as_view(), name="list_post_admin"),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/like/$",
        views.LikePostView.as_view(),
        name="like_post",
    ),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/update/$",
        never_cache(views.UpdatePostView.as_view()),
        name="update_post",
    ),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/delete/$",
        views.DeletePostView.as_view(),
        name="delete_post",
    ),
    re_path(r"^filter/$", views.FilterPostView.as_view(), name="filter_post"),
]


category_urlpatterns = [
    re_path(r"^s/$", views.ListCategoryView.as_view(), name="list_category"),
    re_path(r"add/$", views.AddCategoryView.as_view(), name="add_category"),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/update/$",
        views.UpdateCategoryView.as_view(),
        name="update_category",
    ),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/delete/$",
        views.DeleteCategoryView.as_view(),
        name="delete_category",
    ),
]

tag_urlpatterns = [
    re_path(r"^s/$", views.ListTagView.as_view(), name="list_tag"),
    re_path(r"add/$", views.AddTagView.as_view(), name="add_tag"),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/update/$",
        views.UpdateTagView.as_view(),
        name="update_tag",
    ),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/delete/$",
        views.DeleteTagView.as_view(),
        name="delete_tag",
    ),
]

urlpatterns = [
    re_path(r"^s/", include(post_urlpatterns)),
    re_path(r"^category/", include(category_urlpatterns)),
    re_path(r"^tag/", include(tag_urlpatterns)),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/$",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
]
