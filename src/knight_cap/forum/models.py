from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import F
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_comments.models import Comment

from blog.models import Category, Tag

UserModel = get_user_model()


class Forum(models.Model):
    """A model to represent a forum post."""

    title = models.CharField(_("Title"), max_length=200, unique=True)
    questioner = models.ForeignKey(
        UserModel,
        verbose_name=_("questioner"),
        on_delete=models.SET_NULL,
        related_name="forums",
        help_text=_("The user who asked the question."),
        null=True,
    )
    slug = models.SlugField(
        _("Slug"),
        max_length=200,
        editable=False,
        unique=True,
        help_text=_("Slug will be automaticaly set from forum title."),
    )
    content = RichTextField(_("Question"), help_text=_("Write your question here."))
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="forums",
        help_text=mark_safe(
            _(
                "Choose a category for this question. +"
                "<a href='/forum/s/category/add' target='_blank'>Add new category</a>"
            )
        ),
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        related_name="forums",
        help_text=mark_safe(
            _(
                "Describe what this question is about. "
                "Separate tags with commas. Use existing tags or add new ones. +"
                "<a href='/forum/s/tag/add' target='_blank'>Add new tag</a>"
            )
        ),
    )
    votes = models.ManyToManyField(
        UserModel,
        verbose_name=_("Votes"),
        related_name="voted_forums",
    )
    comments = GenericRelation(
        Comment, related_query_name="post", object_id_field="object_pk"
    )
    enable_comments = models.BooleanField(default=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    class Meta:
        db_table = "forum"
        verbose_name = _("forum")
        verbose_name_plural = _("forums")
        permissions = [("can_vote_answer", "Can vote answer")]
        indexes = [
            models.Index(fields=["slug"], name="forum_slug_idx"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog:update_post", args=(self.slug,))

    def total_votes(self):
        """Returns total number of votes the forum has."""
        return self.votes.count()

    def save(self, *args, **kwargs):
        """Set post title to slug field."""
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)
