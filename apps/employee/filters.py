from django.forms import TextInput
from django_filters import CharFilter, FilterSet, ModelChoiceFilter
from django_select2.forms import ModelSelect2Widget

from apps.employee.models import Doctor, Group


class DoctorFilter(FilterSet):
    personal_record_number = CharFilter(
        lookup_expr="trigram_similar",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Número de registro contiene",
            }
        ),
        label="Número de registro contiene",
    )
    first_name = CharFilter(
        lookup_expr="trigram_similar",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )
    last_name = CharFilter(
        lookup_expr="trigram_similar",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Apellidos contiene"}
        ),
        label="Apellidos contiene",
    )
    group = ModelChoiceFilter(
        queryset=Group.objects.all(),
        widget=ModelSelect2Widget(
            attrs={
                "class": "form-control",
                "data-placeholder": "Grupo de trabajo",
                "data-language": "es",
                "data-theme": "bootstrap-5",
                "data-width": "style",
            },
            search_fields=[
                "name__trigram_similar",
            ],
        ),
        label="Grupo de trabajo",
    )

    class Meta:
        model = Doctor
        fields = [
            "personal_record_number",
            "first_name",
            "last_name",
            "group",
        ]


class GroupFilter(FilterSet):
    name = CharFilter(
        lookup_expr="trigram_similar",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre contiene"}
        ),
        label="Nombre contiene",
    )

    class Meta:
        model = Group
        fields = [
            "name",
        ]
