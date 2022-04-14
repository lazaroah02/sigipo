from django.forms import Select, TextInput
from django_filters import (
    CharFilter,
    ChoiceFilter,
    FilterSet,
    ModelChoiceFilter,
    RangeFilter,
)
from django_filters.widgets import RangeWidget

from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient


class PatientFilter(FilterSet):
    """Filters to search for patients."""

    identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    race = ChoiceFilter(
        choices=Patient.RACE,
        widget=Select(attrs={"class": "form-control", "placeholder": "Raza"}),
    )
    residence_municipality = ModelChoiceFilter(
        queryset=Municipality.objects.all(),
        widget=Select(
            attrs={"class": "form-control", "placeholder": "Municipio de residencia"}
        ),
        label="Municipio de residencia",
    )
    born_municipality = ModelChoiceFilter(
        queryset=Municipality.objects.all(),
        widget=Select(
            attrs={"class": "form-control", "placeholder": "Municipio natal"}
        ),
        label="Municipio natal",
    )
    residence_municipality__province = ModelChoiceFilter(
        queryset=Province.objects.all(),
        widget=Select(
            attrs={"class": "form-control", "placeholder": "Provincia de residencia"}
        ),
        label="Provincia de residencia",
    )
    born_municipality__province = ModelChoiceFilter(
        queryset=Province.objects.all(),
        widget=Select(
            attrs={"class": "form-control", "placeholder": "Provincia natal"}
        ),
        label="Provincia natal",
    )
    age_at_diagnosis = RangeFilter(
        widget=RangeWidget(
            attrs={"class": "form-control", "placeholder": "Edad de diagnostico"}
        ),
        label="Edad de diagnostico",
    )

    class Meta:
        model = Patient
        fields = [
            "identity_card",
            "first_name",
            "last_name",
            "medical_record",
            "race",
            "residence_municipality",
            "born_municipality",
            "age_at_diagnosis",
        ]
