from django import forms
from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    HiddenInput,
    ModelForm,
    NumberInput,
    Select,
    Textarea,
    TextInput,
)
from django_select2.forms import ModelSelect2Widget

from apps.geographic_location.models import Municipality, Province
from apps.patient.models import Patient


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
        choices=Patient.RACE,
        widget=Select(attrs={"class": "form-control"}),
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
    residence_municipality = forms.ModelChoiceField(
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
            search_fields=["name__icontains"],
            dependent_fields={"residence_province": "province"},
        ),
    )
    residence_province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="Provincia de residencia",
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Provincia de residencia",
                "data-language": "es",
                "data-theme": "bootstrap4",
                "data-width": "style",
            },
            search_fields=["name__icontains"],
            max_results=500,
        ),
        required=False,
    )
    born_municipality = forms.ModelChoiceField(
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
            search_fields=["name__icontains"],
            dependent_fields={"residence_province": "province"},
        ),
    )
    born_province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="Provincia natal",
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Provincia natal",
                "data-language": "es",
                "data-theme": "bootstrap4",
                "data-width": "style",
            },
            search_fields=["name__icontains"],
        ),
        required=False,
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
        "residence_province",
    ]

    class Meta:
        model = Patient
        fields = "__all__"


class OncologicPatientForm(BasePatientForm):
    is_oncologic = BooleanField(
        widget=HiddenInput(attrs={"value": "true"}), required=False
    )
