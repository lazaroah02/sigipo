from django.forms import TextInput, DateInput
from django_filters import CharFilter, FilterSet, NumberFilter, DateFilter

from apps.pathological_anatomy.models import (
    Pathology,
)

class PathologyFilter(FilterSet):
    """Filters to search for patients in Radiations."""
        
    patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
        )
    
    patient__first_name = CharFilter(
            lookup_expr="icontains",
            widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
            ),
        label="Nombre contiene",
    )
    
    patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    
    patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    
    authopsy_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. de Tratamiento",
            }
        ),
        label="No. de Tratamiento",
    )
    
    class Meta:
        model = Pathology
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "authopsy_number",
            
        ]