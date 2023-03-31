from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    ChoiceField,
    DateField,
    DateInput,
    Form,
    HiddenInput,
    ModelChoiceField,
    Select,
    TextInput,
)

from apps.core.fields import RelatedModelWrapper
from apps.core.forms import ModelForm
from apps.geographic_location.models import Municipality
from apps.patient.models import Patient, PatientRace, SexChoices


class BasePatientForm(ModelForm):
    """Model to handle patient creation and edition."""

    identity_card = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet de identidad"}
        ),
        label="Carnet de identidad",
        max_length=11,
        min_length=6,
    )
    first_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )
    last_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Apellidos"}),
        label="Apellidos",
    )
    street = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Calle"}),
        label="Calle",
        required=False,
    )
    number = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Número"}),
        label="Número",
        required=False,
    )
    building = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Edificio"}),
        label="Edificio",
        required=False,
    )
    apartment = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Apartamento"}),
        label="Apartamento",
        required=False,
    )
    between_streets = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Entre calles"}
        ),
        label="Entre calles",
        required=False,
    )
    division = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Reparto"}),
        label="Reparto",
        required=False,
    )
    race = ChoiceField(
        choices=PatientRace.choices,
        initial=PatientRace.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Raza",
    )
    sex = ChoiceField(
        choices=SexChoices.choices,
        initial=SexChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sexo",
    )
    date_of_birth = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de nacimiento",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        required=False,
        label="Fecha de nacimiento",
    )
    medical_record = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "No. Historia Clínica"}
        ),
        label="No. Historia Clínica",
        required=False,
    )
    residence_municipality = ModelChoiceField(
        queryset=Municipality.objects.all(),
        label="Municipio de residencia",
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio de residencia",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=["name__trigram_similar", "province__name__trigram_similar"],
        ),
    )
    born_municipality = ModelChoiceField(
        queryset=Municipality.objects.all(),
        label="Municipio natal",
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Municipio natal",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=["name__trigram_similar", "province__name__trigram_similar"],
        ),
    )

    field_order = [
        "identity_card",
        "first_name",
        "last_name",
        "race",
        "sex",
        "date_of_birth",
        "street",
        "number",
        "building",
        "apartment",
        "between_streets",
        "division",
        "medical_record",
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


class NuclearMedicinePatientForm(BasePatientForm):
    is_oncologic = BooleanField(
        widget=HiddenInput(attrs={"value": "false"}), required=False
    )


class PatientChangeStatusForm(Form):
    identity_card = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet de identidad"}
        ),
        label="Carnet de identidad",
        max_length=11,
        min_length=6,
    )


class PatientOncologicReadOnlyForm(OncologicPatientForm):
    """Form tho show Oncologic patient in read only mode."""

    is_oncologic = BooleanField(
        label="¿Es oncológico?",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = True
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs["disabled"] = True
