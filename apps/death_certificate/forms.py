from django.forms import CharField, DateTimeField, DateTimeInput, Textarea

from apps.death_certificate.models import DeathCertificate
from apps.patient.forms import BasePatientForm


class DeathCertificateForm(BasePatientForm):
    """Model to handle DeathCertificate creation and edition."""

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

    class Meta:
        model = DeathCertificate
        fields = "__all__"
