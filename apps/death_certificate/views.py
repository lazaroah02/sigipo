from django.urls import reverse_lazy

from apps.death_certificate.forms import DeathCertificateForm
from apps.death_certificate.models import DeathCertificate
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)


# * death_certificate Views
class DeathCertificateCreateView(BaseCreateView):
    """View to handle DeathCertificate creation."""

    model = DeathCertificate
    form_class = DeathCertificateForm
    success_url = reverse_lazy("death_certificate:death_certificate_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "death_certificate:death_certificate_list"
    permission_required = "accounts.death_certificate_manage"


class DeathCertificateDetailView(BaseDetailView):
    """View to handle DeathCertificate details."""

    model = DeathCertificate
    form_class = DeathCertificateForm
    cancel_url = "death_certificate:death_certificate_list"
    object_not_found_error_message = "Certificado de Defunción no encontrado"
    permission_required = "accounts.death_certificate_manage"


class DeathCertificateUpdateView(BaseUpdateView):
    """View to handle DeathCertificate edition."""

    model = DeathCertificate
    form_class = DeathCertificateForm
    success_url = reverse_lazy("death_certificate:death_certificate_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "death_certificate:death_certificate_list"
    object_not_found_error_message = "Certificado de Defunción no encontrado"
    permission_required = "accounts.death_certificate_manage"


class DeathCertificateDeleteView(BaseDeleteView):
    """View to handle DeathCertificate delete."""

    model = DeathCertificate
    success_url = reverse_lazy("death_certificate:death_certificate_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "death_certificate:death_certificate_list"
    object_not_found_error_message = "Certificado de Defunción no encontrado"
    permission_required = "accounts.death_certificate_manage"
