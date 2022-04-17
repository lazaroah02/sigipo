from django.contrib.admin import ModelAdmin, register

from apps.geographic_location.models import Municipality, Province


@register(Municipality)
class MunicipalityAdmin(ModelAdmin):
    """Municipality Django Admin view."""

    list_display = (
        "name",
        "province",
    )
    list_filter = (
        "name",
        "province",
    )
    search_fields = (
        "name",
        "province__name",
    )
    list_select_related = ("province",)
    list_display_links = ("name",)


register(Province)
