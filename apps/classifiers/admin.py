from django.contrib.admin import ModelAdmin, register

from apps.classifiers.models import Morphology, Topography


@register(Morphology)
class MorphologyAdim(ModelAdmin):
    """Morphology Django Admin view."""

    pass


@register(Topography)
class TopographyAdmin(ModelAdmin):
    """Topography Django Admin view."""

    pass
