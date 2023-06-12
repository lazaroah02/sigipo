from django.contrib.admin import ModelAdmin, register

from apps.radiotherapy.models import (
    Accessories,
    DosimetryPlan,
    Energy,
    Equipment,
    MedicalTurn,
    Prescription,
    RiskOrgans,
    TACStudy,
)


@register(DosimetryPlan)
class DosimetryPlanAdmin(ModelAdmin):
    """DosimetryPlan Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(Energy)
class EnergyAdmin(ModelAdmin):
    """Energy Django Admin view."""

    list_display = ("energy",)
    list_select_related = ("energy",)
    list_display_links = ("energy",)


@register(Equipment)
class EquipmentAdmin(ModelAdmin):
    """Equipment Django Admin view."""

    list_display = ("name",)
    list_select_related = ("name", "energy")
    list_display_links = ("name",)


@register(Accessories)
class AccessoriesAdmin(ModelAdmin):
    """Accessories Django Admin view."""

    list_display = ("name",)
    list_select_related = ("name", "enable_equipment")
    list_display_links = ("name",)


@register(RiskOrgans)
class RiskOrgansAdmin(ModelAdmin):
    """RiskOrgans Django Admin view."""

    list_display = ("name",)
    list_select_related = ("name",)
    list_display_links = ("name",)


@register(Prescription)
class PrescriptionAdmin(ModelAdmin):
    """Prescription Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(MedicalTurn)
class MedicalTurnAdmin(ModelAdmin):
    """MedicalTurn Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)


@register(TACStudy)
class TACStudyAdmin(ModelAdmin):
    """TACStudy Django Admin view."""

    list_display = ("patient",)
    list_select_related = ("patient",)
    list_display_links = ("patient",)
