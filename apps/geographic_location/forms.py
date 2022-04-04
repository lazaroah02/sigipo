from django.forms import CharField, ModelForm, TextInput

from apps.geographic_location.models import Province


class ProvinceForm(ModelForm):
    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Province
        fields = "__all__"
