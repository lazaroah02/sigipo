from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    DateField,
    DateTimeField,
    DateTimeInput,
    FloatField,
    ModelChoiceField,
    ModelMultipleChoiceField,
    NumberInput,
    Textarea,
    TextInput,
    ChoiceField,
    IntegerField,
    BooleanField,
    Select,
)

from django_filters import CharFilter, FilterSet, NumberFilter, ChoiceFilter

from apps.radiotherapy.models import (
    DosimetryPlan,
    Energy,
    Equipment,
    Accessories,
    RiskOrgans,
    Prescription,
    MedicalTurn,
    TACStudy,
    
    AnatomicDataChoices,
    ModalityChoices,
    OAR_TV_TypeChoices,

)

from config.settings.base import FIELD_SEARCH_LOOKUP

class DosimetryPlanFilter(FilterSet):

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )

    modality = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Modalidad",
            }
        ),
        label="Modalidad",
    )

    class Meta:
        model = DosimetryPlan
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "modality",
        ]

class EnergyFilter(FilterSet):
        
    energy = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Energía",
            }
        ),
        label="Energía",
    )
    class Meta:
        model = Energy
        fields = [
            "energy",
        ]

class EquipmentFilter(FilterSet):

    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre del equipo",
            }
        ),
        label="Nombre del equipo",
    )

    modality = ChoiceFilter(
        choices=ModalityChoices.choices,
        widget=Select(
            attrs={
                "class": "form-control form-select",
                "placeholder": "Modalidad",
            }
        ),
        label="Modalidad",
    )

    energy__energy = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Energía",
            }
        ),
        label="Energía",
    )

    class Meta:
        model = Equipment
        fields = [
            "energy__energy",
            "name",
            "modality",
        ]

class AccessoriesFilter(FilterSet):

    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre",
            }
        ),
        label="Nombre",
    )

    type = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Tipo",
            }
        ),
        label="Tipo",
    )

    eid = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ID",
            }
        ),
        label="ID",
    )

    class Meta:
        model = Accessories
        fields = [
            "name",
            "type",
            "id",
        ]

class RiskOrgansFilter(FilterSet):

    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nombre",
            }
        ),
        label="Nombre",
    )

    type = ChoiceFilter(
        choices=OAR_TV_TypeChoices.choices,
        widget=Select(
            attrs={
                "class": "form-control form-select",
                "placeholder": "Tipo de Órganos",
            }
        ),
        label="Tipo de Órganos",
    )

    alpha_beta = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Alpha/Beta",
            }
        ),
        label="Alpha/Beta",
    )

    dosis_limit = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Límite de Dosis",
            }
        ),
        label="Límite de Dosis",
    )

    class Meta:
        model = RiskOrgans
        fields = [
            "name",
            "type",
            "alpha_beta",
            "dosis_limit",
        ]

class PrescriptionFilter(FilterSet):

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )

    treatment_serie = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Serie de Tratamiento",
            }
        ),
        label="Serie de Tratamiento",
    )

    modality = ChoiceFilter(
        choices=ModalityChoices.choices,
        widget=Select(
            attrs={
                "class": "form-control form-select",
                "placeholder": "Modalidad",
            }
        ),
        label="Modalidad",
    )

    class Meta:
        model = Prescription
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]

class MedicalTurnFilter(FilterSet):

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )

    list_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Número de lista",
            }
        ),
        label="Número de lista",
    )

    id = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ID",
            }
        ),
        label="ID",
    )

    class Meta:
        model = MedicalTurn
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "list_number",
            "id",
        ]

class TACStudyFilter(FilterSet):    

    patient__identity_card = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    patient__first_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    patient__last_name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    patient__medical_record = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )

    class Meta:
        model = TACStudy
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ] 