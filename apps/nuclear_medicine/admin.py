# Register your models here.
from django.contrib.admin import ModelAdmin, register

from apps.nuclear_medicine.models import HormonalStudy, OncologicStudy


@register(HormonalStudy)
class HormonalStudyAdmin(ModelAdmin):
    """HormonalStudy Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(OncologicStudy)
class OncologicStudyAdmin(ModelAdmin):
    """OncologicStudy Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)
