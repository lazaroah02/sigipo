from django.contrib.admin import ModelAdmin, register

from apps.death_certificate.models import DeathCertificate


@register(DeathCertificate)
class DeathCertificateAdim(ModelAdmin):
    """DeathCertificate Django Admin view."""

    list_display = ("identity_card",)
    list_select_related = ("identity_card",)
    list_display_links = ("identity_card",)
