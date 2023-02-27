from django.contrib.admin import ModelAdmin, register

from apps.radiations.models import (
    ExternalBeamTreat,
    InternalRadiationTreatment,
    ExternalBeamReg,
    InternalRadiationReg
)


@register(ExternalBeamTreat)
class ExternalBeamTreatAdmin(ModelAdmin):
    """ExternalBeamTreat Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)

@register(InternalRadiationTreatment)
class InternalRadiationTreatmentAdmin(ModelAdmin):
    """InternalRadiationTreatment Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)

@register(ExternalBeamReg)
class ExternalBeamRegAdmin(ModelAdmin):
    """ExternalBeamReg Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)

@register(InternalRadiationReg)
class InternalRadiationRegAdmin(ModelAdmin):
    """InternalRadiationReg Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)
