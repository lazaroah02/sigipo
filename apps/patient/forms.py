from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    ChoiceField,
    Form,
    HiddenInput,
    ModelChoiceField,
    NumberInput,
    Select,
    Textarea,
    TextInput,
)
from django_select2.forms import ModelSelect2Widget

from apps.core.forms import ModelForm
from apps.geographic_location.models import Municipality
from apps.patient.models import Patient, PatientRace


class BasePatientForm(ModelForm):
    """Model to handle patient creation and edition."""

    identity_card = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet de identidad"}
        ),
        label="Carnet de identidad",
        max_length=11,
    )
    first_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )
    last_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Apellidos"}),
        label="Apellidos",
    )
    address = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Dirección actual"}
        ),
        label="Dirección actual",
    )
    race = ChoiceField(
        choices=PatientRace.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Raza",
    )
    medical_record = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "No. Historia Clínica"}
        ),
        label="No. Historia Clínica",
    )
    age_at_diagnosis = CharField(
        widget=NumberInput(
            {"class": "form-control", "placeholder": "Edad al momento del diagnóstico"}
        ),
        label="Edad al momento del diagnóstico",
    )
    residence_municipality = ModelChoiceField(
        queryset=Municipality.objects.all(),
        label="Municipio de residencia",
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio de residencia",
                "data-language": "es",
                "data-theme": "bootstrap4",
                "data-width": "style",
            },
            search_fields=["name__icontains", "province__name__icontains"],
        ),
    )
    born_municipality = ModelChoiceField(
        queryset=Municipality.objects.all(),
        label="Municipio natal",
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio natal",
                "data-language": "es",
                "data-theme": "bootstrap4",
                "data-width": "style",
            },
            search_fields=["name__icontains", "province__name__icontains"],
        ),
    )

    field_order = [
        "identity_card",
        "first_name",
        "last_name",
        "address",
        "race",
        "medical_record",
        "age_at_diagnosis",
        "residence_municipality",
        "born_municipality",
    ]

    class Meta:
        model = Patient
        fields = "__all__"


class OncologicPatientForm(BasePatientForm):
    is_oncologic = BooleanField(
        widget=HiddenInput(attrs={"value": "true"}), required=False
    )


class PatientChangeStatusForm(Form):
    identity_card = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet de identidad"}
        ),
        label="Carnet de identidad",
        max_length=11,
    )
    medical_record = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "No. Historia Clínica"}
        ),
        label="No. Historia Clínica",
    )


class PatientOncologicReadOnlyForm(OncologicPatientForm):
    """Form tho show Oncologic patient in read only mode."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = True
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs["disabled"] = True
