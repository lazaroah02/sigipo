from django.forms import (
    CharField,
    ChoiceField,
    DateTimeField,
    DateTimeInput,
    ModelChoiceField,
    Select,
    Textarea,
    TextInput,
)

from apps.core.fields import RelatedModelWrapper
from apps.core.forms import ModelForm
from apps.core.widget import CauseOfDeathField, CauseOfDeathWidget
from apps.death_certificate.models import (
    CertificationMadeByChoices,
    CivilStateChoices,
    ConfirmationCausesChoices,
    DeathCertificate,
    DeathPlaceChoices,
    LastSurgeriesChoices,
    PregnancyChoices,
    PregnancyResultChoices,
    ResidenceTypeChoices,
    ScholarshipLevelChoices,
    ViolentDeathCausesChoices,
)
from apps.geographic_location.models import Location
from apps.patient.models import Patient
from config.settings.base import FIELD_SEARCH_LOOKUP


class DeathCertificateForm(ModelForm):
    """Model to handle DeathCertificate creation and edition."""

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
    direct_death_cause = CharField(
        widget=Textarea(
            attrs={"class": "form-control", "placeholder": "Causa de Muerte"}
        ),
        label="Causa de Muerte",
    )
    indirect_death_cause_1 = CauseOfDeathField(
        widget=CauseOfDeathWidget(
            attrs={"class": "form-control"},
            cause_attrs={"class": "form-control"},
            date_attrs={"class": "form-control"},
            code_attrs={"class": "form-control"},
        ),
        label="Causa que ocasionó I",
    )
    indirect_death_cause_2 = CauseOfDeathField(
        widget=CauseOfDeathWidget(
            attrs={"class": "form-control"},
            cause_attrs={"class": "form-control"},
            date_attrs={"class": "form-control"},
            code_attrs={"class": "form-control"},
        ),
        label="Causa que ocasionó II",
    )
    indirect_death_cause_3 = CauseOfDeathField(
        widget=CauseOfDeathWidget(
            attrs={"class": "form-control"},
            cause_attrs={"class": "form-control"},
            date_attrs={"class": "form-control"},
            code_attrs={"class": "form-control"},
        ),
        label="Causa que ocasionó III",
    )
    other_contributing_diseases = CauseOfDeathField(
        widget=CauseOfDeathWidget(
            attrs={"class": "form-control"},
            cause_attrs={"class": "form-control"},
            date_attrs={"class": "form-control"},
            code_attrs={"class": "form-control"},
        ),
        label="Otras enfermedades contribuyentes",
    )
    datetime_of_death = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha y hora de defunción",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha y hora de defunción",
    )
    scholarship_level = ChoiceField(
        choices=ScholarshipLevelChoices.choices,
        initial=ScholarshipLevelChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Nivel de Escolaridad",
    )
    civil_state = ChoiceField(
        choices=CivilStateChoices.choices,
        initial=CivilStateChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Estado Cívil",
    )
    residence_type = ChoiceField(
        choices=ResidenceTypeChoices.choices,
        initial=ResidenceTypeChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Tipo de Residencia",
    )
    death_place = ChoiceField(
        choices=DeathPlaceChoices.choices,
        initial=DeathPlaceChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Sitio de Defunción",
    )
    pregnancy = ChoiceField(
        choices=PregnancyChoices.choices,
        initial=PregnancyChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Embarazo en los últimos 12 meses",
    )
    pregnancy_result = ChoiceField(
        choices=PregnancyResultChoices.choices,
        initial=PregnancyResultChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Resultado del embarazo",
    )
    date_of_pregnancy = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha del embarazo",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha del embarazo",
    )
    confirmation_causes = ChoiceField(
        choices=ConfirmationCausesChoices.choices,
        initial=ConfirmationCausesChoices.CLINIC,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación de Causas",
    )
    certification_made_by = ChoiceField(
        choices=CertificationMadeByChoices.choices,
        initial=CertificationMadeByChoices.WATCH,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Certificación realizada por médico de",
    )
    last_surgeries = ChoiceField(
        choices=LastSurgeriesChoices.choices,
        initial=LastSurgeriesChoices.UNDEFINED,
        widget=Select(attrs={"class": "form-control form-select"}),
        label="Cirugías en las últimas 4 semanas",
    )
    violent_death_causes = ChoiceField(
        choices=ViolentDeathCausesChoices.choices,
        initial=ViolentDeathCausesChoices.UNKNOWN,
        widget=Select(attrs={"class": "form-control form-select"}),
        required=False,
        label="Causa aparente de muerte violenta",
    )
    date_of_injury = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de la lesión",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de la lesión",
    )
    place_where_injury_occurred = CharField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Lugar donde ocurrió la lesión",
            }
        ),
        required=False,
        label="Lugar donde ocurrió la lesión",
    )
    event_description = CharField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Descripción de como ocurrió",
            }
        ),
        required=False,
        label="Descripción de como ocurrió",
    )
    requesting_authority = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Autoridad que solicita"}
        ),
        label="Autoridad que solicita",
    )
    act_number = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de Acta"}
        ),
        label="Número de Acta",
    )
    surgery_reasons = CharField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Causa de la Cirugía",
            }
        ),
        label="Razón de la Cirugía",
        required=False,
    )
    death_location = ModelChoiceField(
        queryset=Location.objects.all(),
        label="Localidad de defunción",
        widget=RelatedModelWrapper(
            attrs={
                "class": "form-control",
                "data-placeholder": "Localidad de defunción",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                f"name__{FIELD_SEARCH_LOOKUP}",
                f"province__name__{FIELD_SEARCH_LOOKUP}",
                f"municipality__name__{FIELD_SEARCH_LOOKUP}",
            ],
        ),
    )

    field_order = [
        "patient",
        "scholarship_level",
        "civil_state",
        "residence_type",
        "datetime_of_death",
        "death_place",
        "death_location",
        "direct_death_cause",
        "indirect_death_cause_1",
        "indirect_death_cause_2",
        "indirect_death_cause_3",
        "other_contributing_diseases",
        "confirmation_causes",
        "certification_made_by",
        "last_surgeries",
        "surgery_reasons",
        "pregnancy",
        "pregnancy_result",
        "date_of_pregnancy",
        "violent_death_causes",
        "date_of_injury",
        "place_where_injury_occurred",
        "event_description",
        "requesting_authority",
        "act_number",
    ]

    class Meta:
        model = DeathCertificate
        fields = "__all__"
