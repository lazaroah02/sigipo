from django.forms import CharField, TextInput

from apps.chemotherapy.models import Scheme
from apps.core.forms import ModelForm


class SchemeForm(ModelForm):
    """Model to handle Scheme creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Scheme
        fields = "__all__"
