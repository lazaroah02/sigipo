from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.drugs.filters import DrugFilter, NuclearMedicineDrugFilter
from apps.drugs.models import Drug, NuclearMedicineDrug
from apps.drugs.views import (
    DrugCreateView,
    DrugDeleteView,
    DrugDetailView,
    DrugUpdateView,
    NuclearMedicineDrugCreateView,
    NuclearMedicineDrugDeleteView,
    NuclearMedicineDrugDetailView,
    NuclearMedicineDrugUpdateView,
)

app_name = "drugs"
urlpatterns = [
    # * NuclearMedicineDrug URLs
    path(
        "nuclearmedicinedrug/list/",
        PaginationFilterView.as_view(
            model=NuclearMedicineDrug,
            filterset_class=NuclearMedicineDrugFilter,
            permission_required="accounts.drug_view",
        ),
        name="nuclearmedicinedrug_list",
    ),
    getUrl(NuclearMedicineDrugCreateView),
    getUrl(NuclearMedicineDrugDetailView),
    getUrl(NuclearMedicineDrugUpdateView),
    getUrl(NuclearMedicineDrugDeleteView),
    # * Drug URLs
    path(
        "drug/list/",
        PaginationFilterView.as_view(
            model=Drug,
            filterset_class=DrugFilter,
            permission_required="accounts.drug_view",
        ),
        name="drug_list",
    ),
    getUrl(DrugCreateView),
    getUrl(DrugDetailView),
    getUrl(DrugUpdateView),
    getUrl(DrugDeleteView),
]
