from django.contrib.admin import ModelAdmin, register

from apps.radiotherapy.models import (
    Physicist,
    TACRequest,
)

# Register your models here.

@register(Physicist)
class PhysicistAdmin(ModelAdmin):
    """
    Physicist Django Admin view.
    """

    pass

@register(TACRequest)
class TACRequestAdmin(ModelAdmin):
    """
    TACRequest Django Admin view.
    """

    pass