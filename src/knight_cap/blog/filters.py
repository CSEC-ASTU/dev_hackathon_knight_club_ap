import django_filters
from django.utils.translation import gettext_lazy as _

from blog.models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains", label=_("Title"), distinct=True
    )
    category = django_filters.CharFilter(
        field_name="category__slug",
        lookup_expr="icontains",
        label=_("Category"),
        distinct=True,
    )
    tags = django_filters.CharFilter(
        field_name="tags__slug", lookup_expr="icontains", label=_("Tags"), distinct=True
    )

    class Meta:
        model = Post
        fields = ("title", "category", "tags")
