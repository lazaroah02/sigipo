from django.forms import (
    CharField,
    CheckboxInput,
    CheckboxSelectMultiple,
    DateField,
    DateTimeField,
    DateTimeInput,
    FloatField,
    HiddenInput,
    ModelChoiceField,
    ModelMultipleChoiceField,
    NumberInput,
    Select,
    Textarea,
    TextInput,
    ChoiceField,
    IntegerField,
    BooleanField,
    RadioSelect,
)

from django.utils.safestring import mark_safe
from django_select2.forms import ModelSelect2MultipleWidget
from multiselectfield.forms.fields import MultiSelectFormField


from apps.core.fields import RelatedModelWrapper
from apps.core.forms import ModelForm
from apps.employee.models import Doctor


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

from apps.patient.models import Patient
from config.settings.base import FIELD_SEARCH_LOOKUP


class RTBaseForm(ModelForm):
    """Base class for common fields."""

    patient = ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
                f"identity_card__{FIELD_SEARCH_LOOKUP}",
                f"medical_record__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Paciente",
    )

class RTBaseDetailForm(ModelForm):
    """Base Form to handle common fields."""

    patient = ModelChoiceField(
        queryset=Patient.objects.only_oncologic(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
                f"identity_card__{FIELD_SEARCH_LOOKUP}",
                f"medical_record__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Paciente",
    )

    field_order = [
        "patient",
    ]

    def __init__(self, *args, **kwargs):
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        self.fields["created_date"].widget.attrs = {
            "type": "date",
            "class": "form-control",
            "placeholder": "Fecha",
            "value": kwargs["instance"].created_at.date,
        }

class DosimetryPlanForm(RTBaseForm):

    modality = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Modalidad"}
        ),
        label="Modalidad",
    )

    radiation_therapist_in_charge = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Radioterapeuta a cargo"}
        ),
        label="Radioterapeuta a cargo",
    )

    team = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Radioterapeuta a cargo"}
        ),
        label="Equipo",
    )

    doctor_asigned = ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"first_name__{FIELD_SEARCH_LOOKUP}",
                f"last_name__{FIELD_SEARCH_LOOKUP}",
              ],
        ),
        label="Doctor",
    )

    plan = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Etiqueta del Plan"}
        ),
        label="Etiqueta del Plan",
    )
    
    fractial_dosis = FloatField(widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Dosis por Fracción"}
        ),
        label="Dosis por Fracción",
    )
    total_dosis = FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis Total"}
        ),
        label="Dosis Total",
    )
    session_number = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Número de aplicaciones"}
        ),
        label="Número de aplicaciones",
    )
    anatomic_data_aquisition = ChoiceField(
        label="Adquisición de datos Anatómicos",
        choices=AnatomicDataChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    icru_dosis = FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis en ICRU/Isocentro"}
        ),
        label="Dosis en ICRU/Isocentro",
    )

    max_dosis =  FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis máxima (%)"}
        ),
        label="Dosis máxima (%)",
    )

    field_order = [
        "patient",
    ]

    class Meta:
        
        model = DosimetryPlan
        fields = "__all__"

class EnergyForm(ModelForm):

    energy = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Energía"}
        ),
        label="Energía",
    )

    enable = BooleanField(
            widget=CheckboxInput(attrs={"class": "form-check-input"}),
            required=False,
        label="Habilitado",
    )

    class Meta:
        
        model = Energy
        fields = "__all__"

class EquipmentForm(ModelForm):

    name = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
        label="Nombre",
    )

    modality = ChoiceField(
        label="Modalidad",
        choices=ModalityChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    energy = ModelChoiceField(
        queryset=Energy.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Energía",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"energy__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Energía",
    )

    class Meta:
        
        model = Equipment
        fields = "__all__"

class AccessoriesForm(ModelForm):

    name = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
        label="Nombre",
    )
    
    type = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Tipo"}
        ),
        label="Tipo",
    )
        
    eid = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "ID"}
        ),
        label="ID",
    )

    enable_equipment = ModelChoiceField(
        queryset=Equipment.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Equipo Habilitado",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Equipo Habilitado",
    )

    class Meta:
        
        model = Accessories
        fields = "__all__"


class RiskOrgansForm(ModelForm):

    name = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
        label="Nombre",
    )

    type = ChoiceField(
        label="Tipo",
        choices=ModalityChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    alpha_beta = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "alpha/beta"}
        ),
        label="alpha/beta",
    )

    dosis_limit =  FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis máxima (%)"}
        ),
        label="Dosis máxima (%)",
    )

    class Meta:
        
        model = RiskOrgans
        fields = "__all__"


class PrescriptionForm(RTBaseForm):

    treatment_serie = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Serie del Tratamiento"}
        ),
        label="Serie del Tratamiento",
    )

    modality = ChoiceField(
        label="Modalidad",
        choices=ModalityChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
    )

    status = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Status"}
        ),
        label="Status",
    )

    equipo = ModelChoiceField(
        queryset=Equipment.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Equipo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Equipo",
    )

    irradiate_other_locations = BooleanField(
            widget=CheckboxInput(attrs={"class": "form-check-input"}), required=False,
        label="Otras Localizaciones irradiadas",
    )

    reirradiated_patient = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}), required=False,
        label="Paciente Reirradiado",
    )

    location = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Localizacion"}
        ),
        label="Localizacion",
    )    

    fractial_dosis =  FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis por Fracción"}
        ),
        label="Dosis por Fracción",
    )

    total_dosis =  FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Dosis Total"}
        ),
        label="Dosis Total",
    )

    session_number = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Número de aplicaciones"}
        ),
        label="Número de aplicaciones",
    )

    weekly_session = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Sesión semanal"}
        ),
        label="Sesión semanal",
    )

    daily_session = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Sesión diaria"}
        ),
        label="Sesión diaria",
    )

    organs_at_risk = ModelChoiceField(
        queryset=RiskOrgans.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Órganos en riesgo/ Volúmen diana",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Órganos en riesgo/ Volúmen diana",
    )

    registred_by = ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Registrado por",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Registrado por",
    )

    radiotherapist_in_charge = ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Radioterapeuta a cargo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Radioterapeuta a cargo",
    )

    class Meta:
        
        model = Prescription
        fields = "__all__"


class MedicalTurnForm(RTBaseForm):

    cid = IntegerField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "CID"}
        ),
        label="CID",
    )

    id = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "ID"}
        ),
        label="ID",
    )   

    address = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Dirección"}
        ),
        label="Dirección",
    )   

    location = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Localizacion"}
        ),
        label="Localizacion",
    )   

    stage = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Etapa"}
        ),
        label="Etapa",
    )   

    doctor = ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Doctor",
    )

    waiting_list = BooleanField(
            widget=CheckboxInput(attrs={"class": "form-check-input"}),required=False,
        label="Añadir a la lista de espera",
    )

    date_first_apointment = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de la primera consulta",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de la primera consulta",
    )

    date_culmination_treatment = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de culminación del tratamiento",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de culminación del tratamiento",
    )

    class Meta:
        
        model = MedicalTurn
        fields = "__all__"


class TACStudyForm(RTBaseForm):

    location = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Localización"}
        ),
        label="Localización",
    )   

    chunck_distance =  FloatField(
        widget=NumberInput(
            attrs={"class": "form-control", "placeholder": "Distancia entre cortes (mm)"}
        ),
        label="Distancia entre cortes (mm)",
    )

    patient_position = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Posición del Paciente"}
        ),
        label="Posición del Paciente",
    )   

    protocol = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Protocolo utilizado"}
        ),
        label="Protocolo utilizado",
    )  

    doctor = ModelChoiceField(
        queryset=Doctor.objects.all(),
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Doctor",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
        label="Doctor",
    )

    class Meta:
        
        model = TACStudy
        fields = "__all__"

