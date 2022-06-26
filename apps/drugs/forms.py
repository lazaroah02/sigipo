from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    FloatField,
    NumberInput,
    Select,
    TextInput,
)

from apps.core.forms import ChoiceField as EmptyChoiceField
from apps.core.forms import ModelForm
from apps.drugs.models import (
    Drug,
    DrugTypeChoices,
    NuclearMedicineDrug,
    PresentationChoicesChoices,
    UnitChoicesChoices,
)


class NuclearMedicineDrugForm(ModelForm):
    """Model to handle NuclearMedicineDrug creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = NuclearMedicineDrug
        fields = "__all__"


class DrugForm(ModelForm):
    """Model to handle Drug creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )
    drug_type = CharField(
        widget=Select(
            choices=DrugTypeChoices.choices,
            attrs={"class": "form-control form-select", "placeholder": "Tipo"},
        ),
        label="Tipo",
    )
    presentation = EmptyChoiceField(
        empty_label="----------",
        choices=PresentationChoicesChoices.choices,
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Presentación"},
        ),
        label="Presentación",
        required=False,
    )
    amount = FloatField(
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Cantidad",
            },
        ),
        label="Cantidad",
    )
    unit = EmptyChoiceField(
        choices=UnitChoicesChoices.choices,
        empty_label="----------",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Unidad"},
        ),
        label="Unidad",
        required=False,
    )
    out_of_stock = BooleanField(
        label="¿En falta?",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,
    )

    class Meta:
        model = Drug
        fields = "__all__"
