from django.urls import path

from apps.chemotherapy.filters import ProtocolFilter, SchemeFilter
from apps.chemotherapy.models import Protocol, Scheme
from apps.chemotherapy.views import (
    ProtocolCreateView,
    ProtocolDeleteView,
    ProtocolDetailView,
    ProtocolUpdateView,
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
    # * Protocol URLs
    path(
        "chemotherapy/protocol/list/",
        PaginationFilterView.as_view(
            model=Protocol,
            filterset_class=ProtocolFilter,
            permission_required="chemotherapy_view",
        ),
        name="protocol_list",
    ),
    getUrl(ProtocolCreateView),
    getUrl(ProtocolDetailView),
    getUrl(ProtocolUpdateView),
    getUrl(ProtocolDeleteView),
]
