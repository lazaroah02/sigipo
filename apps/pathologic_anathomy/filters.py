from django.forms import TextInput
from django_filters import (
    CharFilter,
    FilterSet,
    ModelChoiceFilter,
)
from django_select2.forms import ModelSelect2Widget

from apps.employee.models import Doctor
from apps.pathologic_anathomy.models import BiopsyRequest

class BiopsyRequestFilter(FilterSet):
    """Filters to search for Biopsy_Orders."""
    biopsy_id = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Biopsia_ID"}
        ),
        label="Biopsia ID",
    )

    patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    hospital = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Hospital"}
        ),
        label="Hospital",
    )
    health_area = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Area de Salud"}
        ),
        label="Area de Salud",
    )
    biopsy_type = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Tipo de Biopsia"}
        ),
        label="Tipo de Bipsia",
    )
    sample_biopsy = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Tipo de muestra"}
        ),
        label="Muestra",
    )
    medic_that_report = ModelChoiceFilter(
        queryset=Doctor.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Médico que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "first_name__icontains",
                "last_name__icontains",
                "personal_record_number__icontains",
            ],
        ),
        label="Médico que reporta",
    )

    field_order = [
        "hospital",
        "patient__identity_card",
        "biopsy_id",
        "patient__first_name",
        "patient__last_name",
        "patient__medical_record",
        "health_area",
        "biopsy_type",
        "sample_biopsy",
        "medic_that_report",
    ]

    class Meta:
        model = BiopsyRequest
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]

    