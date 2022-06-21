from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.drugs.filters import NuclearMedicineDrugFilter
from apps.drugs.models import NuclearMedicineDrug
from apps.drugs.views import (
    NuclearMedicineDrugCreateView,
    NuclearMedicineDrugDeleteView,
    NuclearMedicineDrugDetailView,
    NuclearMedicineDrugUpdateView,
)

app_name = "drugs"
urlpatterns = [
    # * NuclearMedicineDrug URLs
    path(
        "drug/nuclearmedicinedrug/list/",
        PaginationFilterView.as_view(
            model=NuclearMedicineDrug,
            filterset_class=NuclearMedicineDrugFilter,
            permission_required="drug_view",
        ),
        name="nuclearmedicinedrug_list",
    ),
    getUrl(NuclearMedicineDrugCreateView),
    getUrl(NuclearMedicineDrugDetailView),
    getUrl(NuclearMedicineDrugUpdateView),
    getUrl(NuclearMedicineDrugDeleteView),
]
