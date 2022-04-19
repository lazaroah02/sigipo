from django.urls import path

from apps.core.views import PaginationFilterView
from apps.neoplasm.filters import NeoplasmFilter
from apps.neoplasm.models import Neoplasm
from apps.neoplasm.views import (
    NeoplasmCreateView,
    NeoplasmDeleteView,
    NeoplasmDetailView,
    NeoplasmUpdateView,
)

app_name = "neoplasm"

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
                "add_url": "neoplasm:neoplasm_create",
                "detail_url": "neoplasm:neoplasm_detail",
                "edit_url": "neoplasm:neoplasm_update",
                "delete_url": "neoplasm:neoplasm_delete",
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
