from django.forms import Select, TextInput
from django_filters import CharFilter, ChoiceFilter, FilterSet

from apps.drugs.models import Drug, DrugTypeChoices


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

    class Meta:
        model = Drug
        fields = [
            "name",
            "drug_type",
        ]
