"""auser URL Configuration

	Created by: Wendirad Demelash
	Last modified by: Wendirad Demelash
"""

from django.urls import include, re_path

from auser import views

app_name = "auser"

club_urlpatterns = [
    re_path(r"^$", views.ListActiveClubsView.as_view(), name="list_active_clubs"),
    re_path(
        r"^deactivated/$",
        views.ListDeactivatedClubsView.as_view(),
        name="list_deactivated_clubs",
    ),
    re_path(r"^add/$", views.ClubCreateView.as_view(), name="add_club"),
    re_path(r"^(?P<pk>\d+)/$", views.ClubDetailView.as_view(), name="club_detail"),
    re_path(r"^(?P<pk>\d+)/edit/$", views.UpdateClubView.as_view(), name="edit_club"),
    re_path(
        r"^(?P<pk>\d+)/delete/$", views.DeleteClubView.as_view(), name="delete_club"
    ),
    re_path(
        r"^(?P<pk>\d+)/activate/$",
        views.ActivateClubView.as_view(),
        name="activate_club",
    ),
    re_path(
        r"^(?P<pk>\d+)/deactivate/$",
        views.DeactivateClubView.as_view(),
        name="deactivate_club",
    ),
]

urlpatterns = [
    re_path(r"^club/", include(club_urlpatterns)),
]
