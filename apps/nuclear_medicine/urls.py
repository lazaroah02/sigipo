from django.urls import path

from apps.core.views import PaginationFilterView
from apps.nuclear_medicine.filters import OncologicStudyFilter
from apps.nuclear_medicine.models import PatientOncologicStudy
from apps.nuclear_medicine.views import (
    OncologicStudyCreateView,
    OncologicStudyDeleteView,
    OncologicStudyDetailView,
    OncologicStudyUpdateView,
)

app_name = "nuclear_medicine"
urlpatterns = [
    # * Oncologic Study URLs
    path(
        "oncologic_study/list/",
        PaginationFilterView.as_view(
            model=PatientOncologicStudy,
            filterset_class=OncologicStudyFilter,
            extra_context={
                "crud_name": "Estudio oncológico",
                "crud_instance_name": "estudio oncológico",
                "add_url": "nuclear_medicine:oncologic_study_create",
                "detail_url": "nuclear_medicine:oncologic_study_detail",
                "edit_url": "nuclear_medicine:oncologic_study_update",
                "delete_url": "nuclear_medicine:oncologic_study_delete",
            },
        ),
        name="oncologic_study_list",
    ),
    path(
        "oncologic_study/create/",
        OncologicStudyCreateView.as_view(),
        name="oncologic_study_create",
    ),
    path(
        "oncologic_study/detail/<pk>/",
        OncologicStudyDetailView.as_view(),
        name="oncologic_study_detail",
    ),
    path(
        "oncologic_study/update/<pk>/",
        OncologicStudyUpdateView.as_view(),
        name="oncologic_study_update",
    ),
    path(
        "oncologic_study/delete/<pk>/",
        OncologicStudyDeleteView.as_view(),
        name="oncologic_study_delete",
    ),
]
