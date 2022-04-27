from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    DateField,
    ModelChoiceField,
    TextInput,
)
from django.utils.safestring import mark_safe
from django_select2.forms import ModelSelect2Widget
from multiselectfield.forms.fields import MultiSelectFormField

from apps.core.forms import ModelForm
from apps.nuclear_medicine.models import (
    HormonalStudyChoices,
    OncologicStudyChoices,
    PatientHormonalStudy,
    PatientOncologicStudy,
)
from apps.patient.models import Patient


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    def __init__(self, attrs=None, choices=()):
        self.ignore_check = True
        super().__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(
            html.replace("<ul", "<div")
            .replace("</ul>", "</div>")
            .replace("</li>", "</div>")
            .replace("<li>", '<div class="form-check">')
            .replace("<input", '<input class="form-check-input"')
        )


class CustomReadOnlyCheckboxSelectMultiple(CustomCheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(html.replace("<input", "<input disabled"))


class CustomReadOnlyMultiSelectFormField(MultiSelectFormField):
    widget = CustomReadOnlyCheckboxSelectMultiple


class CustomMultiSelectFormField(MultiSelectFormField):
    widget = CustomCheckboxSelectMultiple


class BaseStudyForm(ModelForm):
    patient = ModelChoiceField(
        queryset=Patient.objects.only_oncologic(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap4",
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


class OncologicStudyForm(ModelForm):
    tests = CustomMultiSelectFormField(
        required=True,
        label="Pruebas",
        choices=OncologicStudyChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        model = PatientOncologicStudy
        fields = "__all__"


class BaseStudyDetailForm(ModelForm):
    patient = ModelChoiceField(
        queryset=Patient.objects.only_oncologic(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Paciente",
                "data-language": "es",
                "data-theme": "bootstrap4",
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
    sample_number = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de muestra"}
        ),
        label="Número de muestra",
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
        "sample_number",
        "patient",
        "created_date",
        "tests",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["created_date"].widget.attrs = {
            "type": "date",
            "class": "form-control",
            "placeholder": "Fecha",
            "value": kwargs["instance"].created_at.date,
        }


class OncologicStudyDetailForm(BaseStudyDetailForm):
    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="Pruebas",
        choices=OncologicStudyChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        model = PatientOncologicStudy
        fields = "__all__"


class HormonalStudyDetailForm(BaseStudyDetailForm):
    tests = CustomReadOnlyMultiSelectFormField(
        required=True,
        label="Pruebas",
        choices=HormonalStudyChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        model = PatientHormonalStudy
        fields = "__all__"


class HormonalStudyForm(ModelForm):
    tests = CustomMultiSelectFormField(
        required=True,
        label="Pruebas",
        choices=HormonalStudyChoices.choices,
        max_length=250,
        max_choices=14,
    )

    class Meta:
        model = PatientHormonalStudy
        fields = "__all__"
