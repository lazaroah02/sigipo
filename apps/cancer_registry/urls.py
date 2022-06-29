from django.urls import path

from apps.cancer_registry.filters import NeoplasmFilter
from apps.cancer_registry.models import Neoplasm
from apps.cancer_registry.views import (
    GroupReportView,
    MorphologyReportView,
    NeoplasmCreateView,
    NeoplasmDeleteView,
    NeoplasmDetailView,
    NeoplasmUpdateView,
    TopographyReportView,
    neoplasm_download_table,
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
            post_function=neoplasm_download_table,
            permission_required="cancer_registry_view",
        ),
        name="neoplasm_list",
    ),
    getUrl(NeoplasmCreateView),
    getUrl(NeoplasmDetailView),
    getUrl(NeoplasmUpdateView),
    getUrl(NeoplasmDeleteView),
    # * Report URLs
    path(
        "report/morphology/",
        MorphologyReportView.as_view(),
        name="morphology_report",
    ),
    path(
        "report/topography/",
        TopographyReportView.as_view(),
        name="topography_report",
    ),
    path(
        "report/group/",
        GroupReportView.as_view(),
        name="group_report",
    ),
]
