from django.contrib.admin import ModelAdmin, register

from apps.drugs.models import Drug


@register(Drug)
class DrugAdmin(ModelAdmin):
    """Drug Django Admin view."""

    pass
