from django.forms import (
    BooleanField,
    CheckboxInput,
    ChoiceField,
    DateField,
    ModelChoiceField,
)
from django.forms.widgets import DateInput, Select
from django_select2.forms import ModelSelect2Widget

from apps.cancer_registry.models import (
    MetastasisChoices,
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
from apps.core.forms import ModelForm
from apps.employee.models import Doctor
from apps.patient.models import Patient


class NeoplasmForm(ModelForm):
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
            }
        ),
        label="Fecha de diagnóstico",
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
    laterality = ChoiceField(
        choices=NeoplasmLateralityChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Lateralidad",
    )
    diagnostic_confirmation = ChoiceField(
        choices=NeoplasmDiagnosticConfirmationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Confirmación del Diagnóstico",
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
    differentiation_grade = ChoiceField(
        choices=NeoplasmDifferentiationGradesChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Grado de diferenciación",
        required=False,
    )
    clinical_extension = ChoiceField(
        choices=NeoplasmClinicalExtensionsChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Extensión clínica",
        required=False,
    )
    clinical_stage = ChoiceField(
        choices=NeoplasmClinicalStageChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Etapa clínica",
    )
    source_of_info = ChoiceField(
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
            }
        ),
        label="Fecha del reporte",
    )
    tumor = ChoiceField(
        choices=TumorChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tumor",
    )
    nodule = ChoiceField(
        choices=NoduleChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nódulo",
    )
    metastasis = ChoiceField(
        choices=MetastasisChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nódulo",
    )
    neoplasm_classification = ChoiceField(
        choices=NeoplasmClassificationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Clínico o Patológico",
    )
    tumor_classification = ChoiceField(
        choices=TumorClassificationChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Clasificación",
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
    treatment_performed = ChoiceField(
        choices=TreatmentPerformedChoices.choices,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tratamiento realizado",
        required=False,
    )

    class Meta:
        model = Neoplasm
        fields = "__all__"
