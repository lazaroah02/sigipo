from django.urls import path

from apps.cancer_registry.filters import NeoplasmFilter, TNMFilter
from apps.cancer_registry.models import TNM, Neoplasm
from apps.cancer_registry.views import (
    NeoplasmCreateView,
    NeoplasmDeleteView,
    NeoplasmDetailView,
    NeoplasmUpdateView,
    TNMCreateView,
    TNMDeleteView,
    TNMDetailView,
    TNMUpdateView,
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
    # * TNM URLs
    path(
        "tnm/list/",
        PaginationFilterView.as_view(
            model=TNM,
            filterset_class=TNMFilter,
            extra_context={
                "crud_name": "TNMs",
                "crud_instance_name": "TNM",
                "add_url": "cancer_registry:tnm_create",
                "detail_url": "cancer_registry:tnm_detail",
                "edit_url": "cancer_registry:tnm_update",
                "delete_url": "cancer_registry:tnm_delete",
            },
            queryset=TNM.objects.all(),
        ),
        name="tnm_list",
    ),
    path(
        "tnm/create/",
        TNMCreateView.as_view(),
        name="tnm_create",
    ),
    path(
        "tnm/detail/<pk>/",
        TNMDetailView.as_view(),
        name="tnm_detail",
    ),
    path(
        "tnm/update/<pk>/",
        TNMUpdateView.as_view(),
        name="tnm_update",
    ),
    path(
        "tnm/delete/<pk>/",
        TNMDeleteView.as_view(),
        name="tnm_delete",
    ),
]
