from django.contrib.admin import ModelAdmin, register

from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography


@register(Morphology)
class MorphologyAdim(ModelAdmin):
    """Morphology Django Admin view."""

    pass


@register(Topography)
class TopographyAdmin(ModelAdmin):
    """Topography Django Admin view."""

    pass


@register(Study)
class StudyAdmin(ModelAdmin):
    """Study Django Admin view."""

    pass


@register(RadioIsotope)
class RadioIsotopeAdmin(ModelAdmin):
    """RadioIsotope Django Admin view."""

    pass
