from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.classifiers.models import Morphology, Topography


class MorphologyFilter(FilterSet):
    """Filters to search for morphologies."""

    code = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Código contiene"}
        ),
    )
    description = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Descripción contiene"}
        ),
    )

    class Meta:
        model = Morphology
        fields = ["code", "description"]


class TopographyFilter(FilterSet):
    """Filters to search for topographies."""

    code = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Código contiene"}
        ),
    )
    description = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Descripción contiene"}
        ),
    )

    class Meta:
        model = Topography
        fields = ["code", "description"]
