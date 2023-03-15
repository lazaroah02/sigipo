from django.contrib.admin import ModelAdmin, register

from apps.chemotherapy.models import (
    Cycle,
    CycleMedication,
    Medication,
    Protocol,
    Scheme,
)


@register(Protocol)
class ProtocolAdmin(ModelAdmin):
    """Protocol Django Admin view."""

    pass


@register(Scheme)
class SchemeDrugAdmin(ModelAdmin):
    """Scheme Django Admin view."""

    pass


@register(Cycle)
class CycleAdmin(ModelAdmin):
    """Cycle Django Admin view."""

    pass


@register(CycleMedication)
class CycleMedicationAdmin(ModelAdmin):
    """CycleMedication Django Admin view."""

    pass


@register(Medication)
class MedicationAdmin(ModelAdmin):
    """Medication Django Admin view."""

    pass
