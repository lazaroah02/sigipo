from django_select2.forms import ModelSelect2Widget

from config.settings.base import FIELD_SEARCH_LOOKUP


class ProvinceWidget(ModelSelect2Widget):
    """Widget to search and select related province."""

    search_fields = [
        f"name__{FIELD_SEARCH_LOOKUP}",
    ]
