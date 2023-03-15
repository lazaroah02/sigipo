from django.forms import TextInput
from django_filters import CharFilter, DateFilter
from apps.patient.filters import PatientFilter

from apps.death_certificate.models import DeathCertificate


class DeathCertificateFilter(PatientFilter):
    """Filters to search for death certificates."""

    date_of_death = DateFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Fecha de Fallecimiento",
    )

    class Meta:
        model = DeathCertificate
        fields = [
            "identity_card",
            "first_name",
            "last_name",
            "medical_record",
            "race",
            "residence_municipality",
            "born_municipality",
            "age_at_diagnosis",
            "is_oncologic",
        ]
