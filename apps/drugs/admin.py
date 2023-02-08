from django.contrib.admin import ModelAdmin, register

from apps.drugs.models import Drug, NuclearMedicineDrug


@register(NuclearMedicineDrug)
class NuclearMedicineDrugAdmin(ModelAdmin):
    """NuclearMedicineDrug Django Admin view."""

    pass


@register(Drug)
class DrugAdmin(ModelAdmin):
    """Drug Django Admin view."""

    pass
