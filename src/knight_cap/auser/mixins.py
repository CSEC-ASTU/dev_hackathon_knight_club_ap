from django.contrib.auth.mixins import AccessMixin


class ClubRequiredMixin(AccessMixin):
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return qs
        return qs.filter(club_id=user.id)


class CurrentUserMixin:
    """A Mixin that automatically add user pk to kwargs, to prevent sending user id over url."""

    pk_kwargs = "pk"

    def setup(self, request, *args, **kwargs):
        kwargs.update({self.pk_kwargs: request.user.pk})
        return super().setup(request, *args, **kwargs)
