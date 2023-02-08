from django.forms import (
    BooleanField,
    CheckboxInput,
    ChoiceField,
    DateField,
    FloatField,
    IntegerField,
    ModelChoiceField,
)
from django.forms.widgets import DateInput, NumberInput, Select
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import (
    AcuteLymphoidLeukemiaChoices,
    AcuteMyeloidLeukemiaChoices,
    ChronicLymphoidLeukemiaChoices,
    ChronicMyeloidLeukemiaChoices,
    MetastasisChoices,
    MultipleMyelomaChoices,
    Neoplasm,
    NeoplasmClassificationChoices,
    NeoplasmClinicalExtensionsChoices,
    NeoplasmClinicalStageChoices,
    NeoplasmDiagnosticConfirmationChoices,
    NeoplasmDifferentiationGradesChoices,
    NeoplasmLateralityChoices,
    NeoplasmSourceOfInfoChoices,
    NoduleChoices,
    TreatmentPerformedChoices,
    TumorChoices,
    TumorClassificationChoices,
)
from apps.classifiers.models import Morphology, Topography
from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.employee.models import Doctor, Group
from apps.patient.models import Patient


class NeoplasmForm(ModelForm):
    """Form for Neoplasm model."""

    patient = ModelChoiceField(
        queryset=Patient.objects.only_oncologic(),
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
    date_of_diagnosis = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de diagnóstico",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        label="Fecha de diagnóstico",
        required=False,
    )
    age_at_diagnosis = IntegerField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Edad al momento de diagnóstico",
            },
        ),
        label="Edad al momento de diagnóstico",
        required=False,
    )
    psa = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "PSA",
            },
        ),
        label="PSA",
        required=False,
    )
    primary_site = ModelChoiceField(
        queryset=Topography.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Sitio primario",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Sitio primario",
    )
    laterality = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmLateralityChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lateralidad",
        required=False,
    )
    diagnostic_confirmation = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmDiagnosticConfirmationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Confirmación del Diagnóstico",
        required=False,
    )
    histologic_type = ModelChoiceField(
        queryset=Morphology.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Tipo histológico",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        label="Tipo histológico",
    )
    differentiation_grade = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmDifferentiationGradesChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Grado de diferenciación",
        required=False,
    )
    clinical_extension = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmClinicalExtensionsChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Extensión clínica",
        required=False,
    )
    clinical_stage = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa clínica",
        required=False,
    )
    source_of_info = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmSourceOfInfoChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Fuente de información",
        required=False,
    )
    is_pregnant = BooleanField(
        label="¿Embarazada?",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    trimester = ChoiceField(
        choices=(
            (1, "Primer trimestre"),
            (2, "Segundo trimestre"),
            (3, "Tercer trimestre"),
            (4, "Cuarto trimestre"),
        ),
        widget=Select(attrs={"class": "form-control"}),
        label="Trimestre",
    )
    is_vih = BooleanField(
        label="¿Es VIH+?",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    date_of_report = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha del reporte",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        required=False,
        label="Fecha del reporte",
    )
    tumor = EmptyChoiceField(
        empty_label="----------",
        choices=TumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tumor",
        required=False,
    )
    nodule = EmptyChoiceField(
        empty_label="----------",
        choices=NoduleChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nódulo",
        required=False,
    )
    metastasis = EmptyChoiceField(
        empty_label="----------",
        choices=MetastasisChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Metástasis",
        required=False,
    )
    neoplasm_classification = EmptyChoiceField(
        empty_label="----------",
        choices=NeoplasmClassificationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Clínico o Patológico",
        required=False,
    )
    tumor_classification = EmptyChoiceField(
        empty_label="----------",
        choices=TumorClassificationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Clasificación",
        required=False,
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
        required=False,
        label="Médico que reporta",
    )
    group = ModelChoiceField(
        queryset=Group.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Grupo que reporta",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__icontains",
            ],
        ),
        required=False,
        label="Grupo que reporta",
    )
    treatment_performed = EmptyChoiceField(
        empty_label="----------",
        choices=TreatmentPerformedChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tratamiento realizado",
        required=False,
    )
    hematological_transformation = BooleanField(
        label="Transformación hematológica",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )
    date_of_first_symptoms = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de primeros síntomas",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        required=False,
        label="Fecha de primeros síntomas",
    )
    acute_lymphoid_leukemia = EmptyChoiceField(
        empty_label="----------",
        choices=AcuteLymphoidLeukemiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Leucemia linfoide aguda (FAB)",
        required=False,
    )
    chronic_lymphoid_leukemia = EmptyChoiceField(
        empty_label="----------",
        choices=ChronicLymphoidLeukemiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Leucemia linfoide crónica (Rail)",
        required=False,
    )
    acute_myeloid_leukemia = EmptyChoiceField(
        empty_label="----------",
        choices=AcuteMyeloidLeukemiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Leucemia mieloide aguda (FAB)",
        required=False,
    )
    multiple_myeloma = EmptyChoiceField(
        empty_label="----------",
        choices=MultipleMyelomaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Mieloma múltiple (Durie-Salmon)",
        required=False,
    )
    chronic_myeloid_leukemia = EmptyChoiceField(
        empty_label="----------",
        choices=ChronicMyeloidLeukemiaChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Leucemia mieloide crónica",
        required=False,
    )

    field_order = [
        "patient",
        "date_of_diagnosis",
        "age_at_diagnosis",
        "primary_site",
        "laterality",
        "histologic_type",
        "psa",
        "tumor",
        "nodule",
        "metastasis",
        "neoplasm_classification",
        "tumor_classification",
        "diagnostic_confirmation",
        "clinical_extension",
        "clinical_stage",
        "differentiation_grade",
        "is_pregnant",
        "trimester",
        "is_vih",
        "hematological_transformation",
        "date_of_first_symptoms",
        "acute_lymphoid_leukemia",
        "chronic_lymphoid_leukemia",
        "acute_myeloid_leukemia",
        "chronic_myeloid_leukemia",
        "multiple_myeloma",
        "source_of_info",
        "group",
        "medic_that_report",
        "date_of_report",
        "treatment_performed",
    ]

    class Meta:
        model = Neoplasm
        fields = "__all__"
        default_permissions = ()
