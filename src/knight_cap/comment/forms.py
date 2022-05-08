from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_comments.forms import CommentForm as ExCommentForm

COMMENT_MAX_LENGTH = getattr(settings, "COMMENT_MAX_LENGTH", 3000)


class CommentForm(ExCommentForm):
    name = None
    email = None
    url = None
    comment = forms.CharField(
        label=_("Comment"),
        widget=forms.Textarea(
            attrs={"class": "form-control", "cols": "10", "rows": "1"}
        ),
        max_length=COMMENT_MAX_LENGTH,
    )

    def get_comment_create_data(self, site_id=None):
        """
        Returns the dict of data to be used to create a comment. Subclasses in
        custom comment apps that override get_comment_model can override this
        method to add extra fields onto a custom comment model.
        """
        self.cleaned_data.update(
            {
                "name": "",
                "email": "",
                "url": "",
            }
        )
        return super().get_comment_create_data(site_id=site_id)
