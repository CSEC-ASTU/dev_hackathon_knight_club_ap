from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group as G
from django.db.models import Q

from auser.models import Division, Club


@receiver(post_save, sender=Division)
def update_division_head_permission(sender, instance=None, created=None, **kwargs):
    instance.head_permissions.set(
        instance.head_permissions.all()
        .order_by()
        .union(instance.members_permissions.all().order_by())
    )

def create_permission_groups(sender, plan, *args, **kwargs):
    Group = apps.get_model("auth", "Group")
    if plan and not Group.objects.filter(name="club").exists():
        Permission = apps.get_model("auth", "Permission")
        club_group = Group.objects.create(name="club")
        club_group_permissions = Permission.objects.filter(
            Q(codename="view_club")
            | Q(codename="change_club")
            | Q(codename="add_division")
            | Q(codename="change_division")
            | Q(codename="view_division")
            | Q(codename="delete_division")
            | Q(codename="add_position")
            | Q(codename="change_position")
            | Q(codename="view_position")
            | Q(codename="delete_position")
            | Q(codename="change_user")
            | Q(codename="view_user")
        )
        club_group.permissions.set(club_group_permissions)

@receiver(post_save, sender=Club)
def add_content_creator_group(sender, instance=None, created=None, **kwargs):
    if created:
        club_group = G.objects.get(name="club")
        instance.user_permissions.set(club_group.permissions.all())
