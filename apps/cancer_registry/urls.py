from django.urls import path

from apps.cancer_registry.filters import NeoplasmFilter
from apps.cancer_registry.models import Neoplasm
from apps.cancer_registry.views import (
    NeoplasmCreateView,
    NeoplasmDeleteView,
    NeoplasmDetailView,
    NeoplasmUpdateView,
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
            permission_required="cancer_registry_view",
        ),
        name="neoplasm_list",
    ),
    getUrl(NeoplasmCreateView),
    getUrl(NeoplasmDetailView),
    getUrl(NeoplasmUpdateView),
    getUrl(NeoplasmDeleteView),
]
