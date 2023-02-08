from django.contrib.admin import ModelAdmin, register

from apps.death_certificate.models import DeathCertificate

@register(DeathCertificate)
class DeathCertificateAdim(ModelAdmin):
    """DeathCertificate Django Admin view."""
    
    pass

