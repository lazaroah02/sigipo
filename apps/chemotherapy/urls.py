from django.urls import path

from apps.chemotherapy.filters import SchemeFilter
from apps.chemotherapy.models import Scheme
from apps.chemotherapy.views import (
    SchemeCreateView,
    SchemeDeleteView,
    SchemeDetailView,
    SchemeUpdateView,
)
from apps.core.views import PaginationFilterView, getUrl

app_name = "chemotherapy"
urlpatterns = [
    # * Scheme URLs
    path(
        "chemotherapy/scheme/list/",
        PaginationFilterView.as_view(
            model=Scheme,
            filterset_class=SchemeFilter,
            permission_required="chemotherapy_view",
        ),
        name="scheme_list",
    ),
    getUrl(SchemeCreateView),
    getUrl(SchemeDetailView),
    getUrl(SchemeUpdateView),
    getUrl(SchemeDeleteView),
]
