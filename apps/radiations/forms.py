from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    DateField,
    DateInput,
    FloatField,
    ModelChoiceField,
    NumberInput,
    Select,
    TextInput,
)
from django.utils.safestring import mark_safe
from django_select2.forms import ModelSelect2Widget
from multiselectfield.forms.fields import MultiSelectFormField

from apps.core.forms import ModelForm
from apps.patient.models import Patient
from apps.radiations.models import (
    ExternalBeamReg,
    ExternalBeamTreat,
    ExternalBeamTreatmentChoices,
    InternalRadiationReg,
    InternalRadiationTreatment,
    InternalRadiationTreatmentChoices,
)


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


class BaseRadiationForm(ModelForm):
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

    biopsy = CharField(
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Biopsia",
            },
        ),
        label="Biopsia",
    )

    dosis = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Dosis",
            },
        ),
        label="Dosis",
    )
    time_table = DateField(
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "Fecha",
            },
        ),
        label="Fecha",
    )
    target_volume = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Volumen Diana",
            },
        ),
        label="Volumen Diana",
    )
    radiation_time = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Tiempo de Radiación",
            },
        ),
        label="Tiempo de Radiación",
    )
    fractionation = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Fraccionamiento",
            },
        ),
        label="Fraccionamiento",
    )
    target_precision = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Precisión al Objetivo",
            },
        ),
        label="Precisión al Objetivo",
    )
    dosis_distribution = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Distribución de Dosis",
            },
        ),
        label="Distribución de Dosis",
    )


class ExternalBeamTreatForm(BaseRadiationForm):
    """Form for ExternalBeamTreat."""

    tests = CustomMultiSelectFormField(
        required=True,
        label="Tratamiento",
        choices=ExternalBeamTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    external_beam_config = CharField(
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Configuración del Haz de Radiación",
            },
        ),
        label="Configuración del Haz de Radiación",
    )

    class Meta:
        """Meta class for ExternalBeamTreatForm."""

        model = ExternalBeamTreat
        fields = "__all__"


class BaseRadiationDetailForm(ModelForm):
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
    treat_number = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de Tratamiento"}
        ),
        label="Número de Tratamiento",
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
        "treat_number",
        "patient",
        "created_date",
        "tests",
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


class ExternalBeamTreatDetailForm(BaseRadiationDetailForm):
    """Form for ExternalBeamTreatDetail."""

    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="",
        choices=ExternalBeamTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        """Meta class for ExternalBeamTreatDetailForm."""

        model = ExternalBeamTreat
        fields = "__all__"


# ***********************************************************************************************************
class ExternalBeamRegForm(BaseRadiationForm):
    """Form for ExternalBeamTreat."""

    treat_number = ModelChoiceField(
        queryset=ExternalBeamReg.objects.all(),
        widget=Select(
            attrs={
                "class": "form-control",
                "placeholder": "Número de tratamiento",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            }
        ),
        label="Número de tratamiento",
    )
    tests = CustomMultiSelectFormField(
        required=True,
        label="Tratamiento",
        choices=InternalRadiationTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    external_beam_config = CharField(
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Configuración del Haz de Radiación",
            },
        ),
        label="Configuración del Haz de Radiación",
    )

    session_number = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Número de Sesión",
            },
        ),
        label="Número de Sesión",
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Form."""

        model = ExternalBeamReg
        fields = "__all__"


class ExternalBeamRegDetailForm(BaseRadiationDetailForm):
    """Form for ExternalBeamTreatDetail."""

    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="",
        choices=ExternalBeamTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Detail Form."""

        model = ExternalBeamReg
        fields = "__all__"


# **********************************Internal Radiation***************************************************************


class InternalRadiationTreatmentForm(BaseRadiationForm):
    """Form for ExternalBeamTreat."""

    tests = CustomMultiSelectFormField(
        required=True,
        label="Tratamiento",
        choices=InternalRadiationTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    radioisotope = CharField(
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Radioisotopo",
            },
        ),
        label="Radioisotopo",
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Form."""

        model = InternalRadiationTreatment
        fields = "__all__"


class InternalRadiationTreatmentDetailForm(BaseRadiationDetailForm):
    """Form for ExternalBeamTreatDetail."""

    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="",
        choices=ExternalBeamTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Detail Form."""

        model = InternalRadiationTreatment
        fields = "__all__"


# ***************************************************************************************
class InternalRadiationRegForm(BaseRadiationForm):
    """Form for ExternalBeamTreat."""

    treat_number = ModelChoiceField(
        queryset=InternalRadiationReg.objects.all(),
        widget=Select(
            attrs={
                "class": "form-control",
                "placeholder": "Número de tratamiento",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            }
        ),
        label="Número de tratamiento",
    )
    tests = CustomMultiSelectFormField(
        required=True,
        label="Tratamiento",
        choices=InternalRadiationTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )
    radioisotope = CharField(
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Radioisotopo",
            },
        ),
        label="Radioisotopo",
    )

    session_number = FloatField(
        widget=NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Número de Sesión",
            },
        ),
        label="Número de Sesión",
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Form."""

        model = InternalRadiationReg
        fields = "__all__"


class InternalRadiationRegDetailForm(BaseRadiationDetailForm):
    """Form for ExternalBeamTreatDetail."""

    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="",
        choices=ExternalBeamTreatmentChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        """Meta class for Internal Radiation Treatment Detail Form."""

        model = InternalRadiationReg
        fields = "__all__"
