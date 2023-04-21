from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.geographic_location.models import Municipality, Province
from config.settings.base import FIELD_SEARCH_LOOKUP


class ProvinceFilter(FilterSet):
    """Filters to search for provinces."""

    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Province
        fields = [
            "name",
        ]


class MunicipalityFilter(FilterSet):
    """Filters to search for municipalities."""

    name = CharFilter(
        lookup_expr=f"{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )
    province = CharFilter(
        lookup_expr=f"name__{FIELD_SEARCH_LOOKUP}",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Provincia contiene"}
        ),
    )

    class Meta:
        model = Municipality
        fields = [
            "name",
            "province",
        ]
