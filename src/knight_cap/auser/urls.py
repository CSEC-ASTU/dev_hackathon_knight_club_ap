"""auser URL Configuration

	Created by: Wendirad Demelash
	Last modified by: Wendirad Demelash
"""

from django.urls import include, re_path

from auser import views

app_name = "auser"

club_urlpatterns = [
    re_path(r"^$", views.ListActiveClubsView.as_view(), name="list_active"),
    re_path(
        r"^deactivated/$",
        views.ListDeactivatedClubsView.as_view(),
        name="list_deactivated",
    ),
    re_path(r"^add/$", views.ClubCreateView.as_view(), name="add"),
    re_path(r"^(?P<pk>\d+)/$", views.ClubDetailView.as_view(), name="detail"),
    re_path(r"^(?P<pk>\d+)/edit/$", views.UpdateClubView.as_view(), name="edit"),
    re_path(r"^(?P<pk>\d+)/delete/$", views.DeleteClubView.as_view(), name="delete"),
    re_path(
        r"^(?P<pk>\d+)/activate/$", views.ActivateClubView.as_view(), name="activate"
    ),
    re_path(
        r"^(?P<pk>\d+)/deactivate/$",
        views.DeactivateClubView.as_view(),
        name="deactivate",
    ),
]

urlpatterns = [
    re_path(r"^club/", include(club_urlpatterns)),
]
