from django.forms import CharField, TextInput

from apps.core.forms import ModelForm
from apps.geographic_location.models import Location, Municipality, Province
from apps.geographic_location.widgets import MunicipalityWidget, ProvinceWidget


class ProvinceForm(ModelForm):
    """Model to handle province creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Province
        fields = "__all__"


class MunicipalityForm(ModelForm):
    """Model to handle municipality creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Municipality
        fields = "__all__"
        widgets = {
            "province": ProvinceWidget(
                attrs={
                    "class": "form-control",
                    "data-placeholder": "Provincias",
                    "data-language": "es",
                    "data-theme": "bootstrap-5",
                    "data-width": "style",
                },
            ),
        }


class LocationForm(ModelForm):
    """Model to handle Location creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Location
        fields = "__all__"
        widgets = {
            "province": ProvinceWidget(
                attrs={
                    "class": "form-control",
                    "data-placeholder": "Provincias",
                    "data-language": "es",
                    "data-theme": "bootstrap-5",
                    "data-width": "style",
                },
            ),
            "municipality": MunicipalityWidget(
                attrs={
                    "class": "form-control",
                    "data-placeholder": "Municipio",
                    "data-language": "es",
                    "data-theme": "bootstrap-5",
                    "data-width": "style",
                },
            ),
        }
