from django import forms

from blog.models import Post


class AddPostForm(forms.ModelForm):
    """A form for creating new posts."""

    class Meta:
        model = Post
        fields = ("title", "content", "category", "tags", "is_draft")
        widgets = {
            "is_draft": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tags": forms.SelectMultiple(
                attrs={"class": "choices form-select multiple-remove"}
            ),
        }


class UpdatePostForm(AddPostForm):
    class Meta(AddPostForm.Meta):
        pass
