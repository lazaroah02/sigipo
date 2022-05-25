# Register your models here.
from django.contrib.admin import ModelAdmin, register

from apps.nuclear_medicine.models import (
    Gammagraphy,
    HormonalResult,
    HormonalStudy,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    SerialIodineDetection,
)


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


@register(HormonalResult)
class HormonalResultAdmin(ModelAdmin):
    """HormonalResult Django Admin view."""

    list_display = ("hormonal_study",)
    list_select_related = ("hormonal_study",)
    list_display_links = ("hormonal_study",)


@register(OncologicResult)
class OncologicResultAdmin(ModelAdmin):
    """OncologicResult Django Admin view."""

    list_display = ("oncologic_study",)
    list_select_related = ("oncologic_study",)
    list_display_links = ("oncologic_study",)


@register(IodineDetection)
class IodineDetectionAdmin(ModelAdmin):
    """IodineDetection Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(SerialIodineDetection)
class SerialIodineDetectionAdmin(ModelAdmin):
    """SerialIodineDetection Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(Gammagraphy)
class GammagraphyAdmin(ModelAdmin):
    """Gammagraphy Django Admin view."""

    list_display = ("patient",)
    list_select_related = (
        "patient",
        "radio_isotope",
    )
    list_display_links = ("patient",)
