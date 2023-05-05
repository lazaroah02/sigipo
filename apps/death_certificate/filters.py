from django.forms import Select, TextInput
from django_filters import (
    CharFilter,
    ChoiceFilter,
    DateFilter,
    FilterSet,
    ModelChoiceFilter,
)
from django_select2.forms import ModelSelect2Widget

from apps.death_certificate.models import ConfirmationCausesChoices, DeathCertificate
from apps.geographic_location.models import Location


class DeathCertificateFilter(FilterSet):
    """Filters to search for death certificates."""

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
    time_of_death = DateFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Fecha de Fallecimiento"}
        ),
        label="Fecha de Fallecimiento",
    )

    confirmation_causes = ChoiceFilter(
        choices=ConfirmationCausesChoices.choices,
        widget=Select(
            attrs={
                "class": "form-control form-select",
                "placeholder": "Confirmación de las causas",
            }
        ),
        label="Confirmación de las causas",
    )

    death_location = ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Localidad de defunción",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
                "locality__name__icontains",
            ],
        ),
        label="Localidad de defunción",
    )

    class Meta:
        model = DeathCertificate
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "time_of_death",
            "confirmation_causes",
            "death_location",
        ]
