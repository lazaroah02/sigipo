from django.forms import CharField, ModelChoiceField, TextInput
from django_select2.forms import ModelSelect2Widget

from apps.core.forms import ModelForm
from apps.employee.models import Doctor, Group


class GroupForm(ModelForm):
    """Model to handle Group creation and edition."""

    name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )

    class Meta:
        model = Group
        fields = "__all__"


class DoctorForm(ModelForm):
    """Model to handle Doctor creation and edition."""

    first_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        label="Nombre",
    )
    last_name = CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Apellidos"}),
        label="Apellidos",
    )
    personal_record_number = CharField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Número de registro"}
        ),
        label="Número de registro",
        max_length=6,
    )
    group = ModelChoiceField(
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
                "name__icontains",
            ],
        ),
        label="Grupo de trabajo",
    )

    class Meta:
        model = Doctor
        fields = "__all__"
