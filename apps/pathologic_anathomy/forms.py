from django.forms import (
    CharField,
    ChoiceField,
    DateField,
    IntegerField,
    ModelChoiceField,
    TextInput,
)
from django.forms.widgets import DateInput, NumberInput, Select
from django_select2.forms import ModelSelect2Widget

from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.employee.models import Doctor
from apps.pathologic_anathomy.models import (
    BiopsyRequest,
    BiopsyTypeChoice,
    HospitalChoice,
    PatientRaceChoice,
)
from apps.patient.models import Patient, SexChoices


class BiopsyRequestForm(ModelForm):
    hospital = EmptyChoiceField(
        empty_label="Seleccionar Hospital",
        choices=HospitalChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Hospital",
        required=False,
    )
    sample_date = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de la muestra",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        required=False,
        label="Fecha de la muestra",
    )
    health_area = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Area de Salud",
                "data-language": "bootstrap-5",
                "data-with": "style",
            },
        ),
        required=False,
        label="Area de Salud",
    )
    especiality = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Especialidad"}
        ),
        required=False,
        label="Especialidad",
    )

    patient = ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "first_name__icontains",
                "last_name__icontains",
                "identity_card__icontains",
                "medical_record__icontains",
            ],
        ),
        label="Paciente",
        required=False,
    )
    age = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Edad del paciente",
            },
        ),
        label="Edad",
        required=False,
    )
    sex = ChoiceField(
        choices=SexChoices.choices,
        initial=SexChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sexo",
    )
    race = ChoiceField(
        choices=PatientRaceChoice.choices,
        initial=PatientRaceChoice.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Raza",
    )
    address = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Direccion particular"}
        ),
        required=False,
        label="Direccion particular",
    )
    biopsy_type = EmptyChoiceField(
        empty_label="Seleccionar Tipo de Biopsia",
        choices=BiopsyTypeChoice.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de biopsia",
        required=False,
    )
    sample_biopsy = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Tipo de muestra"}
        ),
        required=False,
        label="Tipo de muestra",
    )
    clinic_data = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Datos Clinicos"}
        ),
        required=False,
        label="Datos Clinicos",
    )
    clinic_diagnostic = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Diagnostico Clinico"}
        ),
        required=False,
        label="Diagnostico Clinico",
    )
    medic_that_report = ModelChoiceField(
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
        required=False,
    )

    field_order = [
        "hospital",
        "sample_date",
        "health_area",
        "especiality",
        "patient",
        "age",
        "sex",
        "race",
        "address",
        "biopsy_type",
        "sample_biopsy",
        "clinic_data",
        "clinic_diagnostic",
        "medic_that_report",
    ]

    class Meta:
        model = BiopsyRequest
        fields = [
            "hospital",
            "sample_date",
            "health_area",
            "especiality",
            "patient",
            "age",
            "sex",
            "race",
            "address",
            "biopsy_type",
            "sample_biopsy",
            "clinic_data",
            "clinic_diagnostic",
            "medic_that_report",
        ]
        default_permissions = ()
