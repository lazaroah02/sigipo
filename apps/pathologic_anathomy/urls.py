from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.pathologic_anathomy.filters import BiopsyRequestFilter
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.views import (
    BiopsyRequestCreateView,
    BiopsyRequestDeleteView,
    BiopsyRequestDetailView,
    BiopsyRequestUpdateView,
    add_diagnostic_view
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
    path("biopsyrequest/<int:biopsy_pk>/add-diagnostic", 
         add_diagnostic_view,
         name = "biopsyrequest_add_diagnostic"
         ),
    path(
        "biopsy-diagnosticated/list/",
        PaginationFilterView.as_view(
            model=BiopsyRequest,
            queryset=BiopsyRequest.objects.filter(verificated=True),
            filterset_class=BiopsyRequestFilter,
        ),
        name="biopsy-diagnosticated_list",
    ),
]
