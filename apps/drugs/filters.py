from django.forms import Select, TextInput
from django_filters import CharFilter, ChoiceFilter, FilterSet

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
    out_of_stock = ChoiceFilter(
        choices=((True, "En falta"), (False, "Disponible")),
        label="¿En falta?",
        widget=Select(
            attrs={"class": "form-control form-select", "placeholder": "¿En falta?"}
        ),
    )

    class Meta:
        model = Drug
        fields = [
            "name",
            "drug_type",
            "out_of_stock",
        ]
