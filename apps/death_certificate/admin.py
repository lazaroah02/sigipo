from django.contrib.admin import ModelAdmin, register

from apps.death_certificate.models import DeathCertificate


@register(DeathCertificate)
class DeathCertificateAdmin(ModelAdmin):
    """DeathCertificate Django Admin view."""

    list_display = ("direct_death_cause",)
    list_select_related = ("direct_death_cause",)
    list_display_links = ("direct_death_cause",)
