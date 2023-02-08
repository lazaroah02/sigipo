from django.forms import CharField, TextInput

from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography
from apps.core.forms import ModelForm


class MorphologyForm(ModelForm):
    """Model to handle morphology creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Morphology
        fields = "__all__"


class TopographyForm(ModelForm):
    """Model to handle topography creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Topography
        fields = "__all__"


class StudyForm(ModelForm):
    """Model to handle studies creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Study
        fields = "__all__"


class RadioIsotopeForm(ModelForm):
    """Model to handle radio isotopes creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = RadioIsotope
        fields = "__all__"
