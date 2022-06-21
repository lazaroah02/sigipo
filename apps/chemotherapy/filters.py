from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.chemotherapy.models import Scheme


class SchemeFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Scheme
        fields = [
            "name",
        ]
