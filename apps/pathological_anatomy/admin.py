from django.contrib.admin import ModelAdmin, register

from apps.pathological_anatomy.models import (
    Pathology,
)

@register(Pathology)
class PathologyAdmin(ModelAdmin):
    """ExternalBeamTreat Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)
