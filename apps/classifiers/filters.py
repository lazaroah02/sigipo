from django.forms import TextInput
from django_filters import CharFilter, FilterSet

from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography


class MorphologyFilter(FilterSet):
    """Filters to search for morphologies."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Morphology
        fields = ["name"]


class TopographyFilter(FilterSet):
    """Filters to search for topographies."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Topography
        fields = ["name"]


class StudyFilter(FilterSet):
    """Filters to search for studies."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = Study
        fields = [
            "name",
        ]


class RadioIsotopeFilter(FilterSet):
    """Filters to search for radio isotopes."""

    name = CharFilter(
        lookup_expr="icontains",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
    )

    class Meta:
        model = RadioIsotope
        fields = [
            "name",
        ]
