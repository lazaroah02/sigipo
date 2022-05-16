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
from apps.core.views import PaginationFilterView, getUrl

app_name = "cancer_registry"

urlpatterns = [
    # * Neoplasm URLs
    path(
        "neoplasm/list/",
        PaginationFilterView.as_view(
            model=Neoplasm,
            filterset_class=NeoplasmFilter,
            queryset=Neoplasm.objects.all(),
        ),
        name="neoplasm_list",
    ),
    getUrl(NeoplasmCreateView),
    getUrl(NeoplasmDetailView),
    getUrl(NeoplasmUpdateView),
    getUrl(NeoplasmDeleteView),
    # * TNM URLs
    path(
        "tnm/list/",
        PaginationFilterView.as_view(
            model=TNM,
            filterset_class=TNMFilter,
            queryset=TNM.objects.all(),
        ),
        name="tnm_list",
    ),
    getUrl(TNMCreateView),
    getUrl(TNMDetailView),
    getUrl(TNMUpdateView),
    getUrl(TNMDeleteView),
]
