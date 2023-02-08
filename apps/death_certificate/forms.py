from django.forms import CharField,DateField, DateInput, Textarea, TextInput

from apps.death_certificate.models import DeathCertificate
# from apps.core.forms import ModelForm
from apps.patient.forms import BasePatientForm


class DeathCertificateForm(BasePatientForm):
    """Model to handle DeathCertificate creation and edition."""

    death_cause = CharField(
        widget=Textarea(attrs={"class": "form-control", "placeholder": "Causa de Muerte"}),
        label="Causa de Muerte",
    )
    
    date_of_death = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Fecha de defunción",
                "type": "date",
            },
            format="%Y-%m-%d",
        ),
        required=False,
        label="Fecha de defunción",
    )

    time_of_death = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Hora de defunción",
                "type": "date",
            }
        ),
        required=False,
        label="Hora de defunción",
    )

    class Meta:
        model = DeathCertificate
        fields = "__all__"
