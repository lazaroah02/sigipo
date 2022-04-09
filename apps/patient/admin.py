from django.contrib.admin import ModelAdmin, site

from apps.patient.models import Patient


class PatientAdmin(ModelAdmin):
    """Municipality Django Admin view."""

    list_display = ("identity_card", "first_name", "last_name", "address")
    list_filter = ("born_municipality", "residence_municipality")
    search_fields = (
        "identity_card",
        "first_name",
        "last_name",
    )
    list_select_related = ("born_municipality", "residence_municipality")
    list_display_links = ("first_name", "last_name")


site.register(Patient, PatientAdmin)
