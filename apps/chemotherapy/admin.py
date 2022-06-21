from django.contrib.admin import ModelAdmin, register

from apps.chemotherapy.models import Protocol, Scheme


@register(Protocol)
class ProtocolDrugAdmin(ModelAdmin):
    """Protocol Django Admin view."""

    pass


@register(Scheme)
class SchemeDrugAdmin(ModelAdmin):
    """Scheme Django Admin view."""

    pass
