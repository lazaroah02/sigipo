from django.urls import path

from apps.chemotherapy.filters import MedicationFilter, ProtocolFilter, SchemeFilter
from apps.chemotherapy.models import Medication, Protocol, Scheme
from apps.chemotherapy.views import (
    MedicationCreateView,
    MedicationDeleteView,
    MedicationDetailView,
    MedicationUpdateView,
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
    # * Medication URLs
    path(
        "chemotherapy/medication/list/",
        PaginationFilterView.as_view(
            model=Medication,
            filterset_class=MedicationFilter,
            permission_required="chemotherapy_view",
        ),
        name="medication_list",
    ),
    getUrl(MedicationCreateView),
    getUrl(MedicationDetailView),
    getUrl(MedicationUpdateView),
    getUrl(MedicationDeleteView),
]
