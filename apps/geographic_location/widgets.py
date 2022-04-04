from django_select2.forms import ModelSelect2Widget


class ProvinceWidget(ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]
