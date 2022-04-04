from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.geographic_location.models import Province


class ProvinceFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Province
        fields = [
            "name",
        ]
