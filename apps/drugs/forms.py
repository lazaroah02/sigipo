from django.forms import CharField, Select, TextInput

from apps.core.forms import ModelForm
from apps.drugs.models import Drug, DrugTypeChoices


class DrugForm(ModelForm):
    """Model to handle Drugs creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )
    drug_type = CharField(
        widget=Select(
            choices=DrugTypeChoices.choices,
            attrs={"class": "form-control form-select", "placeholder": "Tipo"},
        ),
    )

    class Meta:
        model = Drug
        fields = "__all__"
