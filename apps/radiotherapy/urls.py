from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.radiotherapy.filters import (
    DosimetryPlanFilter,
    EnergyFilter,
    EquipmentFilter,
    AccessoriesFilter,
    RiskOrgansFilter,
    PrescriptionFilter,
    MedicalTurnFilter,
    TACStudyFilter,
)
from apps.radiotherapy.models import (
    DosimetryPlan,
    Energy,
    Equipment,
    Accessories,
    RiskOrgans,
    Prescription,
    MedicalTurn,
    TACStudy,
)
from apps.radiotherapy.views import (
    DosimetryPlanCreateView,
    DosimetryPlanDetailView,
    DosimetryPlanUpdateView,
    DosimetryPlanDeleteView,
    EnergyCreateView,
    EnergyDetailView,
    EnergyUpdateView,
    EnergyDeleteView,
    EquipmentCreateView,
    EquipmentDetailView,
    EquipmentUpdateView,
    EquipmentDeleteView,
    AccessoriesCreateView,
    AccessoriesDetailView,
    AccessoriesUpdateView,
    AccessoriesDeleteView,
    RiskOrgansCreateView,
    RiskOrgansDetailView,
    RiskOrgansUpdateView,
    RiskOrgansDeleteView,
    PrescriptionCreateView,
    PrescriptionDetailView,
    PrescriptionUpdateView,
    PrescriptionDeleteView,
    MedicalTurnCreateView,
    MedicalTurnDetailView,
    MedicalTurnUpdateView,
    MedicalTurnDeleteView,
    TACStudyCreateView,
    TACStudyDetailView,
    TACStudyUpdateView,
    TACStudyDeleteView,
)

app_name = "radiotherapy"
urlpatterns = [
    # * radiotherapy URLs
    path(
        "dosimetryplan/list/",
        PaginationFilterView.as_view(
            model=DosimetryPlan,
            filterset_class=DosimetryPlanFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="DosimetryPlan_list",
    ),
    getUrl(DosimetryPlanCreateView),
    getUrl(DosimetryPlanDetailView),
    getUrl(DosimetryPlanUpdateView),
    getUrl(DosimetryPlanDeleteView),

    path(
        "energy/list/",
        PaginationFilterView.as_view(
            model=Energy,
            filterset_class=EnergyFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="Energy_list",
    ),
    getUrl(EnergyCreateView),
    getUrl(EnergyDetailView),
    getUrl(EnergyUpdateView),
    getUrl(EnergyDeleteView),

    path(
        "equipment/list/",
        PaginationFilterView.as_view(
            model=Equipment,
            filterset_class=EquipmentFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="Equipment_list",
    ),
    getUrl(EquipmentCreateView),
    getUrl(EquipmentDetailView),
    getUrl(EquipmentUpdateView),
    getUrl(EquipmentDeleteView),

    path(
        "accessories/list/",
        PaginationFilterView.as_view(
            model=Accessories,
            filterset_class=AccessoriesFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="Accessories_list",
    ),
    getUrl(AccessoriesCreateView),
    getUrl(AccessoriesDetailView),
    getUrl(AccessoriesUpdateView),
    getUrl(AccessoriesDeleteView),

    path(
        "riskorgans/list/",
        PaginationFilterView.as_view(
            model=RiskOrgans,
            filterset_class=RiskOrgansFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="RiskOrgans_list",
    ),
    getUrl(RiskOrgansCreateView),
    getUrl(RiskOrgansDetailView),
    getUrl(RiskOrgansUpdateView),
    getUrl(RiskOrgansDeleteView),

    path(
        "prescription/list/",
        PaginationFilterView.as_view(
            model=Prescription,
            filterset_class=PrescriptionFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="Prescription_list",
    ),
    getUrl(PrescriptionCreateView),
    getUrl(PrescriptionDetailView),
    getUrl(PrescriptionUpdateView),
    getUrl(PrescriptionDeleteView),

    path(
        "medicalTurn/list/",
        PaginationFilterView.as_view(
            model=MedicalTurn,
            filterset_class=MedicalTurnFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="MedicalTurn_list",
    ),
    getUrl(MedicalTurnCreateView),
    getUrl(MedicalTurnDetailView),
    getUrl(MedicalTurnUpdateView),
    getUrl(MedicalTurnDeleteView),

    path(
        "TACStudy/list/",
        PaginationFilterView.as_view(
            model=TACStudy,
            filterset_class=TACStudyFilter,
            permission_required="accounts.radiotherapy_view",
        ),
        name="TACStudy_list",
    ),
    getUrl(TACStudyCreateView),
    getUrl(TACStudyDetailView),
    getUrl(TACStudyUpdateView),
    getUrl(TACStudyDeleteView),

    ]
