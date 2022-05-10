from django.forms import TextInput
from django_filters import CharFilter, FilterSet, NumberFilter

from apps.nuclear_medicine.models import (
    HormonalResult,
    IodineDetection,
    OncologicResult,
    PatientHormonalStudy,
    PatientOncologicStudy,
    SerialIodineDetection,
)


class OncologicStudyFilter(FilterSet):
    """Filters to search for patients."""

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
    sample_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. de muestra",
            }
        ),
        label="No. de muestra",
    )

    class Meta:
        model = PatientOncologicStudy
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "sample_number",
        ]


class HormonalStudyFilter(FilterSet):
    """Filters to search for patients."""

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
    sample_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. de muestra",
            }
        ),
        label="No. de muestra",
    )

    class Meta:
        model = PatientHormonalStudy
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
            "sample_number",
        ]


class HormonalResultFilter(FilterSet):
    """Filters to search for patients."""

    hormonal_study__patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    hormonal_study__patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    hormonal_study__patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    hormonal_study__patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    hormonal_study__sample_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. de muestra",
            }
        ),
        label="No. de muestra",
    )

    class Meta:
        model = HormonalResult
        fields = [
            "hormonal_study__patient__identity_card",
            "hormonal_study__patient__first_name",
            "hormonal_study__patient__last_name",
            "hormonal_study__patient__medical_record",
            "hormonal_study__sample_number",
        ]


class OncologicResultFilter(FilterSet):
    """Filters to search for patients."""

    oncologic_study__patient__identity_card = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Carnet contiene"}
        ),
        label="Carnet contiene",
    )
    oncologic_study__patient__first_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    oncologic_study__patient__last_name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    oncologic_study__patient__medical_record = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. historia clínica contiene",
            }
        ),
        label="No. historia clínica contiene",
    )
    oncologic_study__sample_number = NumberFilter(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "No. de muestra",
            }
        ),
        label="No. de muestra",
    )

    class Meta:
        model = OncologicResult
        fields = [
            "oncologic_study__patient__identity_card",
            "oncologic_study__patient__first_name",
            "oncologic_study__patient__last_name",
            "oncologic_study__patient__medical_record",
            "oncologic_study__sample_number",
        ]


class SerialIodineDetectionFilter(FilterSet):
    """Filters to search for patients."""

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

    class Meta:
        model = SerialIodineDetection
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]


class IodineDetectionFilter(FilterSet):
    """Filters to search for patients."""

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

    class Meta:
        model = IodineDetection
        fields = [
            "patient__identity_card",
            "patient__first_name",
            "patient__last_name",
            "patient__medical_record",
        ]
