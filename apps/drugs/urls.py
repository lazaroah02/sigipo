from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.drugs.filters import DrugFilter
from apps.drugs.models import Drug
from apps.drugs.views import (
    DrugCreateView,
    DrugDeleteView,
    DrugDetailView,
    DrugUpdateView,
)

app_name = "drugs"
urlpatterns = [
    # * Drug URLs
    path(
        "drug/list/",
        PaginationFilterView.as_view(
            model=Drug,
            filterset_class=DrugFilter,
        ),
        name="drug_list",
    ),
    getUrl(DrugCreateView),
    getUrl(DrugDetailView),
    getUrl(DrugUpdateView),
    getUrl(DrugDeleteView),
]
