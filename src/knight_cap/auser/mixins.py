from django.contrib.auth.mixins import AccessMixin


class ClubRequiredMixin(AccessMixin):
	def get_queryset(self):
		qs = super().get_queryset()
		user = self.request.user
		if user.is_superuser:
			return qs
		return qs.filter(club_id=user.id)