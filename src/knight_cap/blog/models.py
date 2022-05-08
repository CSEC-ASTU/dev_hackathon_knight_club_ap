from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_comments.models import Comment
from django_comments.moderation import CommentModerator, moderator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    description = models.TextField(verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name=_("Creator"), null=True
    )

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Save slug field."""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("blog:update_category", kwargs={"slug": self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    description = models.TextField(verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name=_("Creator"), null=True
    )

    class Meta:
        db_table = "tags"
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Save slug field."""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("blog:update_tag", kwargs={"slug": self.slug})


class Post(models.Model):
    """A model for blog posts."""

    title = models.CharField(_("Title"), max_length=200, unique=True)
    slug = models.SlugField(
        _("Slug"),
        max_length=200,
        editable=False,
        unique=True,
        help_text=_("Slug will be automaticaly set from post title."),
    )
    content = RichTextField(
        _("Post content"),
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        help_text=mark_safe(
            _(
                "Choose a category for this post. +"
                "<a href='/post/s/category/add' target='_blank'>Add new category</a>"
            )
        ),
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tags"),
        related_name="posts",
        help_text=mark_safe(
            _(
                "Describe what this post is about. "
                "Separate tags with commas. Use existing tags or add new ones. +"
                "<a href='/post/s/tag/add' target='_blank'>Add new tag</a>"
            )
        ),
    )
    is_draft = models.BooleanField(
        _("Save as draft"),
        default=False,
        help_text=_("If true, this post will not be available to end users."),
    )
    likes = models.ManyToManyField(
        User, verbose_name=_("Post likes"), related_name="liked_posts"
    )
    comments = GenericRelation(
        Comment, related_query_name="post", object_id_field="object_pk"
    )
    enable_comments = models.BooleanField(
        default=True,
        help_text=_(
            "False, the comment will simply be disallowed (i.e., immediately deleted)."
        ),
    )
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        db_table = "post"
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        permissions = [("can_like_post", "Can like post")]
        indexes = [
            models.Index(fields=["slug"], name="post_slug_idx"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog:update_post", args=(self.slug,))

    def total_likes(self):
        """Returns total number of likes the post have."""
        return self.likes.count()

    def save(self, *args, **kwargs):
        """Set post title to slug field."""
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)


class PostModerator(CommentModerator):
    enable_field = "enable_comments"


moderator.register(Post, PostModerator)
