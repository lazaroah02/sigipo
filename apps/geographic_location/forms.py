from django.forms import CharField, ModelForm, TextInput

from apps.geographic_location.models import Municipality, Province
from apps.geographic_location.widgets import ProvinceWidget


class ProvinceForm(ModelForm):
    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Province
        fields = "__all__"


class MunicipalityForm(ModelForm):
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
                    "data-theme": "bootstrap4",
                },
            ),
        }
