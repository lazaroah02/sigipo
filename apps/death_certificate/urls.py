from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.death_certificate.filters import DeathCertificateFilter
from apps.death_certificate.models import DeathCertificate
from apps.death_certificate.views import (
    DeathCertificateCreateView,
    DeathCertificateDeleteView,
    DeathCertificateDetailView,
    DeathCertificateUpdateView,
)

app_name = "death_certificate"
urlpatterns = [
    # * death_certificate URLs
    path(
        "death_certificate/list/",
        PaginationFilterView.as_view(
            model=DeathCertificate,
            filterset_class=DeathCertificateFilter,
            permission_required="accounts.death_certificate_view",
        ),
        name="death_certificate_list",
    ),
    getUrl(DeathCertificateCreateView),
    getUrl(DeathCertificateDetailView),
    getUrl(DeathCertificateUpdateView),
    getUrl(DeathCertificateDeleteView),
]
