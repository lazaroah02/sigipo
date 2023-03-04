from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    DateField,
    DateInput,
    FloatField,
    ModelChoiceField,
    NumberInput,
    Textarea,
    TextInput,    
)

from django.utils.safestring import mark_safe
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from multiselectfield.forms.fields import MultiSelectFormField

from apps.core.forms import ModelForm
from apps.pathological_anatomy.models import (
    Pathology,
    OtherClinicalDiagnosesChoices
)
from apps.patient.models import Patient


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    """Widget to render checkbox in bootstrap style."""

    def __init__(self, attrs=None, choices=()):
        """Initialize the widget."""
        self.ignore_check = True
        super().__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget."""
        html = super().render(name, value, attrs, renderer)
        return mark_safe(
            html.replace("<ul", "<div")
            .replace("</ul>", "</div>")
            .replace("</li>", "</div>")
            .replace("<li>", '<div class="form-check">')
            .replace("<input", '<input class="form-check-input"')
        )


class CustomReadOnlyCheckboxSelectMultiple(CustomCheckboxSelectMultiple):
    """Widget to render checkbox in bootstrap style in readonly mode."""

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget."""
        html = super().render(name, value, attrs, renderer)
        return mark_safe(html.replace("<input", "<input disabled"))


class CustomReadOnlyMultiSelectFormField(MultiSelectFormField):
    """Custom form field width custom bootstrap styled widget."""

    widget = CustomReadOnlyCheckboxSelectMultiple


class CustomMultiSelectFormField(MultiSelectFormField):
    """Custom form field width custom bootstrap styled widget."""

    widget = CustomCheckboxSelectMultiple


class PathologyForm(ModelForm):
    """Base class for common Radioations fields."""

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

    authopsy_number  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Número de Autopsia",
            },
        ),
        label="Número de Autopsia",
    )

    entry_date = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha de ingreso",
            },
        ),
        label="Fecha de ingreso",
    )

    exit_date = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha de egreso",
            },
        ),
        label="Fecha de egreso",
    )

    eval_speciality  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Egreso (Especialidad)",
            },
        ),
        label="Egreso (Especialidad)",
    )

    eviseration_date = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha de eviseración",
            },
        ),
        label="Fecha de eviseración",
    )

    eviseration_by  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Por (Eviseración)",
            },
        ),
        label="Por (Eviseración)",
    )

    disection_date = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha de disección",
            },
        ),
        label="Fecha de disección",
    )

    disection_by  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Por (Disección)",
            },
        ),
        label="Por (Disección)",
    )

    dignostic_date = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha de diagnóstico",
            },
        ),
        label="Fecha de diagnóstico",
    )

    diagnostic_by  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Por (Diagnóstico)",
            },
        ),
        label="Por (Diagnóstico)",
    )

    study_full  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Estudio Completo",
            },
        ),
        label="Estudio Completo",
    )
    
    study_micro  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Estudio Micro",
            },
        ),
        label="Estudio Micro",
    )

    hc_resume  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Resumen de Historia Clínica",
            },
        ),
        label="Resumen de Historia Clínica",
    )

####################################Clinicacl Diagnose ######################################

    CDM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CDM",
            },
        ),
        label="Diagnóstico Clínico CDM",
    )

    CiM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CIM",
            },
        ),
        label="Diagnóstico Clínico CIM",
    )

    CIM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CIM",
            },
        ),
        label="Diagnóstico Clínico CIM",
    )

    CBM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CBM",
            },
        ),
        label="Diagnóstico Clínico CBM",
    )

    CC  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CC",
            },
        ),
        label="Diagnóstico Clínico CC",
    )

    CC  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CC",
            },
        ),
        label="Diagnóstico Clínico CC",
    )

    tests = CustomMultiSelectFormField(
        required=True,
        label="Otros Diagnosticos Clínicos",
        choices=OtherClinicalDiagnosesChoices.choices,
        max_length=250,
        max_choices=14,
    )

#############################################################################################

    external_habit  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Hábito externo",
            },
        ),
        label="Hábito externo",
    )

    internal_habit  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Hábito interno",
            },
        ),
        label="Hábito interno",
    )
    
    cavities  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Cavidades",
            },
        ),
        label="Cavidades",
    )
    
    nerv_sistem  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Sistema Nervioso",
            },
        ),
        label="Sistema Nervioso",
    )
    
    respiratory_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Respiratorio",
            },
        ),
        label="Aparato Respiratorio",
    )
    
    cardiovascular_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Cardiovascular",
            },
        ),
        label="Aparato Cardiovascular",
    )
    
    digestive_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Disgestivo",
            },
        ),
        label="Aparato Disgestivo",
    )
    
    urinal_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Urinario",
            },
        ),
        label="Aparato Urinario",
    )
    
    genital_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Genital",
            },
        ),
        label="Aparato Genital",
    )
    
    hemollymphoietic_aparatus  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Aparato Hemolinfopoyético",
            },
        ),
        label="Aparato Hemolinfopoyético",
    )
    
    endocrine_system  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Sistema Endocrino",
            },
        ),
        label="Sistema Endocrino",
    )
    
    osteo_mio_articular_system  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Sistema Osteo-Mio-Articular",
            },
        ),
        label="Sistema Osteo-Mio-Articular",
    )

########################################Mesurements#########################################   
    
    brain_weight = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Cerebro",
            },
        ),
        label="Peso del Cerebro",
    )

    cerebellum_stream_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso Cerebelo y Tallo",
            },
        ),
        label="Peso Cerebelo y Tallo",
    )
    right_lung_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Pulmón derecho",
            },
        ),
        label="Peso del Pulmón derecho",
    )
    left_lung_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Pulmón izquierdo",
            },
        ),
        label="Peso del Pulmón izquierdo",
    )
    heart_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Corazón",
            },
        ),
        label="Peso del Corazón",
    )
    VI = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "VI (mm)",
            },
        ),
        label="VI (mm)",
    )
    VD = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "VD (mm)",
            },
        ),
        label="VD (mm)",
    )
    t_valve = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Válvula T (mm)",
            },
        ),
        label="Válvula T (mm)",
    )
    p_valve = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Válvula P (mm)",
            },
        ),
        label="Válvula P (mm)",
    )
    M = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "M (mm)",
            },
        ),
        label="M (mm)",
    )
    A = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "A (mm)",
            },
        ),
        label="A (mm)",
    )
    liver_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Hígado",
            },
        ),
        label="Peso del Hígado",
    )
    r_kidney_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Riñón derecho",
            },
        ),
        label="Peso del Riñón derecho",
    )
    r_kidney_v = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Volumen del Riñón derecho",
            },
        ),
        label="Volumen del Riñón derecho",
    )
    l_kidney_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Riñón izquierdo",
            },
        ),
        label="Peso del Riñón izquierdo",
    )
    l_kidney_v = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Volumen del Riñón izquierdo",
            },
        ),
        label="Volumen del Riñón izquierdo",
    )
    pancreas_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Páncreas",
            },
        ),
        label="Peso del Páncreas",
    )
    spleen_w = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Bazo",
            },
        ),
        label="Peso del Bazo",
    )
    thyroid = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Peso del Tiroides",
            },
        ),
        label="Peso del Tiroides",
    )

####################################################################################################

    macroscopic_conclusions  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Conclusiones Macroscópicas",
            },
        ),
        label="Conclusiones Macroscópicas",
    )

####################################Final Anatopathologic Dignose############################# 
    
    CDM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CDM",
            },
        ),
        label="Diagnóstico Clínico CDM",
    )

    CiM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CIM",
            },
        ),
        label="Diagnóstico Clínico CIM",
    )

    CIM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CIM",
            },
        ),
        label="Diagnóstico Clínico CIM",
    )

    CBM  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CBM",
            },
        ),
        label="Diagnóstico Clínico CBM",
    )

    CC  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CC",
            },
        ),
        label="Diagnóstico Clínico CC",
    )

    CC  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Diagnóstico Clínico CC",
            },
        ),
        label="Diagnóstico Clínico CC",
    ) 

    other_anatopathologic_dignose  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Otros Diagnósticos Anatopatológicos",
            },
        ),
        label="Otros Diagnósticos Anatopatológicos",
    ) 
    
    
###############################################################################################   

    observation_epicrisis  = CharField(
        widget=Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Observaciones (Epicrisis)",
            },
        ),
        label="Observaciones (Epicrisis)",
    )

    pathologist  = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Patólogo",
            },
        ),
        label="Patólogo",
    )

    class Meta:
        """Meta class for PathologyForm."""

        model = Pathology
        fields = "__all__"



class PathologyDetailForm(ModelForm):
    """BaseRadiationDetailForm to handle common fields."""

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
    authopsy_number = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de Autopsia"}
        ),
        label="Número de Autopsia",
    )
    created_date = DateField(
        widget=TextInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha",
            },
        ),
        label="Fecha",
    )

    field_order = [
        "authopsy_number",
        "patient",
        "created_date",
        "tests",
    ]


    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="",
        choices=OtherClinicalDiagnosesChoices.choices,
        max_length=250,
        max_choices=14,
    )

    def __init__(self, *args, **kwargs):
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        self.fields["created_date"].widget.attrs = {
            "type": "date",
            "class": "form-control",
            "placeholder": "Fecha",
            "value": kwargs["instance"].created_at.date,
        }

    class Meta:
        """Meta class for ExternalBeamTreatDetailForm."""

        model = Pathology
        fields = "__all__"