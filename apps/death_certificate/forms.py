from django.forms import CharField, TextInput, DateTimeField, DateTimeInput, Textarea, ModelChoiceField,Select

from apps.death_certificate.models import DeathCertificate
from apps.patient.forms import BasePatientForm
from apps.pathological_anatomy.models import Pathology


class DeathCertificateForm(BasePatientForm):
    """Model to handle DeathCertificate creation and edition."""

    deathCertificate_number = CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Número de Certificación de Defunción",
            },
        ),
        label="Número de Certificación de Defunción",
    )
    
    death_cause = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa de Muerte"}),
        label="Causa de Muerte",
    )
    
    time_of_death = DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de defunción",
                "type": "date",
            },
            format="%Y-%m-%d %H:%M",
        ),
        required=False,
        label="Fecha de defunción",
    )

    authopsy_number = ModelChoiceField(
        queryset=Pathology.objects.all(),
        widget= Select(
            attrs = {
            "class": "form-control",
            "placeholder": "Número de autopsia",
            "data-theme": "bootstrap-5",
            "data-width": "style",
            }
        ),
        label="Número de autopsia",
    )

    class Meta:
        model = DeathCertificate
        fields = "__all__"
