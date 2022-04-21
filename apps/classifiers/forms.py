from django.forms import CharField, TextInput

from apps.classifiers.models import Morphology, Topography
from apps.core.forms import ModelForm


class MorphologyForm(ModelForm):
    """Model to handle morphology creation and edition."""

    code = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Código"}),
        label="Código",
    )
    description = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Descripción"}),
        label="Descripción",
    )

    class Meta:
        model = Morphology
        fields = "__all__"


class TopographyForm(ModelForm):
    """Model to handle topography creation and edition."""

    code = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Código"}),
        label="Código",
    )
    description = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Descripción"}),
        label="Descripción",
    )

    class Meta:
        model = Topography
        fields = "__all__"
