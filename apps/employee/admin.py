# Register your models here.

from django.contrib.admin import ModelAdmin, register

from apps.employee.models import Doctor, Group


@register(Doctor)
class DoctorAdmin(ModelAdmin):
    """Doctor Django Admin view."""

    pass


@register(Group)
class GroupAdmin(ModelAdmin):
    """Group Django Admin view."""

    pass
