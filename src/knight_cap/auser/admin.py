from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from auser.models import Club, Division, Position, User


@admin.register(Club)
class ClubAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("name", "username", "password")}),
        (_("club info"), {"fields": ("email", "phone_number", "location", "po_box")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "username",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    exclude = ("date_joined",)


# admin.site.register(Club)
admin.site.register(User)
admin.site.register(Division)
admin.site.register(Position)
