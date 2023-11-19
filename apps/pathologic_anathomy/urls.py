from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.pathologic_anathomy.filters import BiopsyRequestFilter
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.views import (
    BiopsyDiagnosticatedDeleteView,
    BiopsyRequestCreateView,
    BiopsyRequestDeleteView,
    BiopsyRequestDetailView,
    BiopsyRequestUpdateView,
    add_diagnostic_view,
    biopsy_diagnostic_update_view,
    biopsy_diagnosticated_detail_view,
)

app_name = "pathologic_anathomy"

# * FormularioBiopsy result urls
urlpatterns = [
    path(
        "biopsyrequest/list/",
        PaginationFilterView.as_view(
            model=BiopsyRequest,
            queryset=BiopsyRequest.objects.filter(verificated=False),
            filterset_class=BiopsyRequestFilter,
        ),
        name="biopsyrequest_list",
    ),
    getUrl(BiopsyRequestCreateView),
    getUrl(BiopsyRequestDetailView),
    getUrl(BiopsyRequestUpdateView),
    getUrl(BiopsyRequestDeleteView),
    path(
        "biopsyrequest/<int:biopsy_pk>/add-diagnostic",
        add_diagnostic_view,
        name="biopsyrequest_add_diagnostic",
    ),
    path(
        "biopsy-diagnosticated/list/",
        PaginationFilterView.as_view(
            model=BiopsyRequest,
            queryset=BiopsyRequest.objects.filter(verificated=True),
            filterset_class=BiopsyRequestFilter,
            template_name="pathologic_anathomy/biopsys_diagnosticated_filter.html",
        ),
        name="biopsy-diagnosticated_list",
    ),
    path(
        "biopsy-diagnosticated/<int:biopsy_pk>/detail/",
        biopsy_diagnosticated_detail_view,
        name="biopsy_diagnosticated_detail",
    ),
    path(
        "biopsy-diagnosticated/<int:biopsy_pk>/update/",
        biopsy_diagnostic_update_view,
        name="biopsy_diagnostic_update",
    ),
    path(
        "biopsy-diagnosticated/delete/<int:pk>/",
        BiopsyDiagnosticatedDeleteView.as_view(),
        name="biopsy_diagnosticated_delete",
    ),
]
