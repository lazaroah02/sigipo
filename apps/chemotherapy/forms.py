from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    FloatField,
    IntegerField,
    ModelChoiceField,
    NumberInput,
    Select,
    TextInput,
)
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import Protocol, RoomChoices, Scheme
from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.employee.models import Doctor
from apps.patient.models import Patient


class SchemeForm(ModelForm):
    """Model to handle Scheme creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Scheme
        fields = "__all__"


class ProtocolForm(ModelForm):
    """Model to handle Protocol creation and edition."""

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
    )
    scheme = ModelChoiceField(
        queryset=Scheme.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Esquema",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Esquema",
    )
    room = EmptyChoiceField(
        empty_label="----------",
        choices=RoomChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lugar",
    )
    height = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Talla (cm)",
            },
        ),
        label="Talla (cm)",
    )
    weight = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Peso (Kg)",
            },
        ),
        label="Peso (Kg)",
    )
    cycles = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ciclos",
            },
        ),
        label="Ciclos",
    )
    stage = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa",
    )
    doctor = ModelChoiceField(
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
    suspended = BooleanField(
        label="Suspendido",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    class Meta:
        model = Protocol
        fields = "__all__"
