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
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/$",
        views.ClubDetailView.as_view(),
        name="club_detail",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/edit/$",
        views.UpdateClubView.as_view(),
        name="edit_club",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/delete/$",
        views.DeleteClubView.as_view(),
        name="delete_club",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/activate/$",
        views.ActivateClubView.as_view(),
        name="activate_club",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/deactivate/$",
        views.DeactivateClubView.as_view(),
        name="deactivate_club",
    ),
    re_path(
        r"^(?P<club_name>[-a-zA-Z0-9_]+)/division/add/$",
        views.DivisionCreateView.as_view(),
        name="add_division",
    ),
]

division_urlpatterns = [
    re_path(
        r"^add/(?P<division_slug>[-a-zA-Z0-9_]+)/$",
        views.DivisionCreateView.as_view(),
        name="add_sub_division",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/$",
        views.DivisionDetailView.as_view(),
        name="division_detail",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/edit/$",
        views.DivisionUpdateView.as_view(),
        name="edit_division",
    ),
    re_path(
        r"^(?P<slug>[-a-zA-Z0-9_]+)/delete/$",
        views.DeleteDivisionView.as_view(),
        name="delete_division",
    ),
]

urlpatterns = [
    re_path(r"^profile/edit/$", views.ProfileEditView.as_view(), name="profile_edit"),
    re_path(r"^club/", include(club_urlpatterns)),
    re_path(r"^division/", include(division_urlpatterns)),
]
