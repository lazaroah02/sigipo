from django.forms import (
    CharField,
    CheckboxSelectMultiple,
    DateField,
    FloatField,
    ModelChoiceField,
    NumberInput,
    TextInput,
)
from django.utils.safestring import mark_safe
from django_select2.forms import ModelSelect2Widget
from multiselectfield.forms.fields import MultiSelectFormField

from apps.core.forms import ModelForm
from apps.nuclear_medicine.models import (
    HormonalResult,
    HormonalStudyChoices,
    OncologicResult,
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


class OncologicStudyForm(BaseStudyForm):
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


class HormonalStudyForm(BaseStudyForm):
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


class OncologicResultForm(ModelForm):
    oncologic_study = ModelChoiceField(
        queryset=PatientOncologicStudy.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Estudio Oncológico",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__icontains",
                "patient__last_name__icontains",
                "patient__identity_card__icontains",
                "patient__medical_record__icontains",
                "sample_number",
            ],
        ),
        label="Estudio Oncológico",
    )
    tsh = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "TSH"}),
        label="TSH",
        required=False,
    )
    t3 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T3"}),
        label="T3",
        required=False,
    )
    t4 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T4"}),
        label="T4",
        required=False,
    )
    tg = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "TG"}),
        label="TG",
        required=False,
    )
    anti_tg = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "ANTI-TG"}),
        label="ANTI-TG",
        required=False,
    )
    anti_tipo = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "ANTI-TIPO"}),
        label="ANTI-TIPO",
        required=False,
    )
    calcit = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CALCIT"}),
        label="CALCIT",
        required=False,
    )
    ca19_9 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CA 19-9"}),
        label="CA 19-9",
        required=False,
    )
    ca15_3 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CA 15-3"}),
        label="CA 15-3",
        required=False,
    )
    ca125 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CA 125"}),
        label="CA 125",
        required=False,
    )
    cea = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CEA"}),
        label="CEA",
        required=False,
    )
    alf = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "ALF"}),
        label="ALF",
        required=False,
    )
    psa = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "PSA"}),
        label="PSA",
        required=False,
    )
    psafree = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "PSA FREE"}),
        label="PSA FREE",
        required=False,
    )

    class Meta:
        model = OncologicResult
        fields = "__all__"


class HormonalResultForm(ModelForm):
    hormonal_study = ModelChoiceField(
        queryset=PatientHormonalStudy.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Estudio hormonal",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "patient__first_name__icontains",
                "patient__last_name__icontains",
                "patient__identity_card__icontains",
                "patient__medical_record__icontains",
                "sample_number",
            ],
        ),
        label="Estudio hormonal",
    )
    tsh = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "TSH"}),
        label="TSH",
        required=False,
    )
    t3 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T3"}),
        label="T3",
        required=False,
    )
    t4 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T4"}),
        label="T4",
        required=False,
    )
    t3f = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T3F"}),
        label="T3F",
        required=False,
    )
    t4f = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "T4F"}),
        label="T4F",
        required=False,
    )
    prl = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "PRL"}),
        label="PRL",
        required=False,
    )
    fsh = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "FSH"}),
        label="FSH",
        required=False,
    )
    lh = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "LH"}),
        label="LH",
        required=False,
    )
    prg = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "PRG"}),
        label="PRG",
        required=False,
    )
    e2 = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "E2"}),
        label="E2",
        required=False,
    )
    cort = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "CORT"}),
        label="CORT",
        required=False,
    )
    ins = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "INS"}),
        label="INS",
        required=False,
    )
    test = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "TEST"}),
        label="TEST",
        required=False,
    )
    gh = FloatField(
        widget=NumberInput(attrs={"class": "form-control", "placeholder": "GH"}),
        label="GH",
        required=False,
    )

    class Meta:
        model = HormonalResult
        fields = "__all__"
