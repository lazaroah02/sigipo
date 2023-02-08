from django.urls import path

from apps.chemotherapy.filters import (
    CycleFilter,
    MedicationFilter,
    ProtocolFilter,
    SchemeFilter,
)
from apps.chemotherapy.models import Cycle, Medication, Protocol, Scheme
from apps.chemotherapy.views import (
    CycleCreateView,
    CycleDeleteView,
    CycleDetailView,
    CycleUpdateView,
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
        "scheme/list/",
        PaginationFilterView.as_view(
            model=Scheme,
            filterset_class=SchemeFilter,
            permission_required="accounts.chemotherapy_view",
        ),
        name="scheme_list",
    ),
    getUrl(SchemeCreateView),
    getUrl(SchemeDetailView),
    getUrl(SchemeUpdateView),
    getUrl(SchemeDeleteView),
    # * Protocol URLs
    path(
        "protocol/list/",
        PaginationFilterView.as_view(
            model=Protocol,
            filterset_class=ProtocolFilter,
            permission_required="accounts.chemotherapy_view",
        ),
        name="protocol_list",
    ),
    getUrl(ProtocolCreateView),
    getUrl(ProtocolDetailView),
    getUrl(ProtocolUpdateView),
    getUrl(ProtocolDeleteView),
    # * Medication URLs
    path(
        "medication/list/",
        PaginationFilterView.as_view(
            model=Medication,
            filterset_class=MedicationFilter,
            permission_required="accounts.chemotherapy_view",
        ),
        name="medication_list",
    ),
    getUrl(MedicationCreateView),
    getUrl(MedicationDetailView),
    getUrl(MedicationUpdateView),
    getUrl(MedicationDeleteView),
    # * Cycle URLs
    path(
        "cycle/list/",
        PaginationFilterView.as_view(
            queryset=Cycle.objects.prefetch_related(
                "cyclemedication_set"
            ).select_related("protocol__scheme", "protocol__patient"),
            filterset_class=CycleFilter,
            permission_required="accounts.chemotherapy_view",
        ),
        name="cycle_list",
    ),
    getUrl(CycleCreateView),
    getUrl(CycleUpdateView),
    getUrl(CycleDetailView),
    getUrl(CycleDeleteView),
]
