from django.urls import path

from apps.core.views import PaginationFilterView
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
            extra_context={
                "crud_name": "Fármacos",
                "crud_instance_name": "fármaco",
                "add_url": "drugs:drug_create",
                "detail_url": "drugs:drug_detail",
                "edit_url": "drugs:drug_update",
                "delete_url": "drugs:drug_delete",
            },
        ),
        name="drug_list",
    ),
    path(
        "drug/create/",
        DrugCreateView.as_view(),
        name="drug_create",
    ),
    path(
        "drug/detail/<pk>/",
        DrugDetailView.as_view(),
        name="drug_detail",
    ),
    path(
        "drug/update/<pk>/",
        DrugUpdateView.as_view(),
        name="drug_update",
    ),
    path(
        "drug/delete/<pk>/",
        DrugDeleteView.as_view(),
        name="drug_delete",
    ),
]
