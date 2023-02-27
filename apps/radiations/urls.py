from django.urls import path

from apps.core.views import PaginationFilterView, getUrl

from apps.radiations.filters import (
    ExternalBeamTreatFilter,
    InternalRadiationTreatmentFilter,
    ExternalBeamRegFilter,
    InternalRadiationRegFilter
)

from apps.radiations.models import (
    ExternalBeamTreat,
    InternalRadiationTreatment,
    ExternalBeamReg,
    InternalRadiationReg
)

from apps.radiations.views import (
    ExternalBeamTreatCreateView,
    ExternalBeamTreatDetailView,
    ExternalBeamTreatUpdateView,
    ExternalBeamTreatDeleteView,
    InternalRadiationTreatCreateView,
    InternalRadiationTreatDetailView,
    InternalRadiationTreatUpdateView,
    InternalRadiationTreatDeleteView,
    ExternalBeamRegCreateView,
    ExternalBeamRegDetailView,
    ExternalBeamRegUpdateView,
    ExternalBeamRegDeleteView,
    InternalRadiationRegCreateView,
    InternalRadiationRegDetailView,
    InternalRadiationRegUpdateView,
    InternalRadiationRegDeleteView

)

app_name = "radiations"
urlpatterns = [
    # * External Beam URLs
    path(
        "external_beam/list/",
        PaginationFilterView.as_view(
            model=ExternalBeamTreat,
            filterset_class=ExternalBeamTreatFilter,
            permission_required="accounts.radiations_view",
        ),
        name="external_beam_treat_list",
    ),
    getUrl(ExternalBeamTreatCreateView),
    getUrl(ExternalBeamTreatDetailView),
    getUrl(ExternalBeamTreatUpdateView),
    getUrl(ExternalBeamTreatDeleteView),
    
    
    path(
        "internal_radiation/list/",
        PaginationFilterView.as_view(
            model=InternalRadiationTreatment,
            filterset_class=InternalRadiationTreatmentFilter,
            permission_required="accounts.radiations_view",
        ),
        name="internal_radiation_list",
    ),
    getUrl(InternalRadiationTreatCreateView),
    getUrl(InternalRadiationTreatDetailView),
    getUrl(InternalRadiationTreatUpdateView),
    getUrl(InternalRadiationTreatDeleteView),

    path(
        "external_beam_reg/list/",
        PaginationFilterView.as_view(
            queryset=ExternalBeamReg.objects.select_related(
                "patient"
            ).all(),
            filterset_class=ExternalBeamRegFilter,
            permission_required="accounts.radiations_view",
        ),
        name="external_beam_reg_list",
    ),
    getUrl(ExternalBeamRegCreateView),
    getUrl(ExternalBeamRegDetailView),
    getUrl(ExternalBeamRegUpdateView),
    getUrl(ExternalBeamRegDeleteView),

    path(
        "internal_radiation_reg/list/",
        PaginationFilterView.as_view(
            queryset=InternalRadiationReg.objects.select_related(
                "internal_radiation__patient"
            ).all(),
            filterset_class=InternalRadiationRegFilter,
            permission_required="accounts.radiations_view",
        ),
        name="internal_radiation_reg_list",
    ),
    getUrl(InternalRadiationRegCreateView),
    getUrl(InternalRadiationRegDetailView),
    getUrl(InternalRadiationRegUpdateView),
    getUrl(InternalRadiationRegDeleteView),
]