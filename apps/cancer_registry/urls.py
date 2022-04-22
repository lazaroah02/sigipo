from django.urls import path

from apps.cancer_registry.filters import NeoplasmFilter
from apps.cancer_registry.models import Neoplasm
from apps.cancer_registry.views import (
    NeoplasmCreateView,
    NeoplasmDeleteView,
    NeoplasmDetailView,
    NeoplasmUpdateView,
)
from apps.core.views import PaginationFilterView

app_name = "cancer_registry"

urlpatterns = [
    # * Neoplasm URLs
    path(
        "neoplasm/list/",
        PaginationFilterView.as_view(
            model=Neoplasm,
            filterset_class=NeoplasmFilter,
            extra_context={
                "crud_name": "Neoplasias",
                "crud_instance_name": "neoplasia",
                "add_url": "cancer_registry:neoplasm_create",
                "detail_url": "cancer_registry:neoplasm_detail",
                "edit_url": "cancer_registry:neoplasm_update",
                "delete_url": "cancer_registry:neoplasm_delete",
            },
            queryset=Neoplasm.objects.all(),
        ),
        name="neoplasm_list",
    ),
    path(
        "neoplasm/create/",
        NeoplasmCreateView.as_view(),
        name="neoplasm_create",
    ),
    path(
        "neoplasm/detail/<pk>/",
        NeoplasmDetailView.as_view(),
        name="neoplasm_detail",
    ),
    path(
        "neoplasm/update/<pk>/",
        NeoplasmUpdateView.as_view(),
        name="neoplasm_update",
    ),
    path(
        "neoplasm/delete/<pk>/",
        NeoplasmDeleteView.as_view(),
        name="neoplasm_delete",
    ),
]
