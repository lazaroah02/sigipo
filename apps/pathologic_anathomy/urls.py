from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.pathologic_anathomy.filters import BiopsyRequestFilter
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.views import (
    BiopsyRequestCreateView,
    BiopsyRequestDeleteView,
    BiopsyRequestDetailView,
    BiopsyRequestUpdateView,
    BiopsyRequestAddDiagnosticView
)

app_name = "pathologic_anathomy"

# * FormularioBiopsy result urls
urlpatterns = [
    path(
        "biopsyrequest/list/",
        PaginationFilterView.as_view(
            model=BiopsyRequest,
            queryset=BiopsyRequest.objects.filter(verificated = False),
            filterset_class=BiopsyRequestFilter,
        ),
        name="biopsyrequest_list",
    ),
    getUrl(BiopsyRequestCreateView),
    getUrl(BiopsyRequestDetailView),
    getUrl(BiopsyRequestUpdateView),
    getUrl(BiopsyRequestDeleteView),
    path("biopsyrequest/add-diagnostic", BiopsyRequestAddDiagnosticView.as_view()),
    
    path(
        "biopsy-verificated/list/",
        PaginationFilterView.as_view(
            model=BiopsyRequest,
            queryset=BiopsyRequest.objects.filter(verificated=True),
            filterset_class=BiopsyRequestFilter,
        ),
        name="biopsy-verificated_list",
    ),
    
]
