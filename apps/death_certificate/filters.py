from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.death_certificate.models import DeathCertificate


class DeathCertificateFilter(FilterSet):
    """Filters to search for death certificates."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = DeathCertificate
        fields = ["name"]

