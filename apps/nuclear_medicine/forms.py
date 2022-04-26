from django.forms import ModelChoiceField
from django_select2.forms import ModelSelect2Widget

from apps.core.forms import ModelForm
from apps.nuclear_medicine.models import PatientOncologicStudy
from apps.patient.models import Patient


class OncologicStudyForm(ModelForm):
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

    class Meta:
        model = PatientOncologicStudy
        fields = "__all__"
