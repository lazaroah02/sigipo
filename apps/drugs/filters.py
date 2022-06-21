from django.forms import CheckboxInput, Select, TextInput
from django_filters import BooleanFilter, CharFilter, ChoiceFilter, FilterSet

from apps.drugs.models import Drug, DrugTypeChoices, NuclearMedicineDrug


class NuclearMedicineDrugFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = NuclearMedicineDrug
        fields = [
            "name",
        ]


class DrugFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )
    drug_type = ChoiceFilter(
        choices=DrugTypeChoices.choices,
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "Tipo"}
        ),
    )
    out_of_stock = BooleanFilter(
        widget=CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Drug
        fields = [
            "name",
            "drug_type",
            "out_of_stock",
        ]
