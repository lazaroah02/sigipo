from django.forms import Select, TextInput
from django_filters import CharFilter, ChoiceFilter, FilterSet, ModelChoiceFilter
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import NeoplasmClinicalStageChoices
from apps.chemotherapy.models import Protocol, RoomChoices, Scheme
from apps.employee.models import Doctor


class SchemeFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Scheme
        fields = [
            "name",
        ]


class ProtocolFilter(FilterSet):
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
    scheme = ChoiceFilter(
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa",
    )
    room = ChoiceFilter(
        choices=RoomChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lugar",
    )
    stage = ChoiceFilter(
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa",
    )
    doctor = ModelChoiceFilter(
        queryset=Doctor.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Grupo que reporta",
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
        label="Grupo que reporta",
    )
    suspended = ChoiceFilter(
        choices=((True, "Suspendido"), (False, "Activo")),
        label="Suspendido",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Suspendido"}
        ),
    )

    class Meta:
        model = Protocol
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "scheme",
            "room",
            "stage",
            "doctor",
            "suspended",
        ]
