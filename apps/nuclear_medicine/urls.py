from django.urls import path

from apps.core.views import PaginationFilterView
from apps.nuclear_medicine.filters import HormonalStudyFilter, OncologicStudyFilter
from apps.nuclear_medicine.models import PatientHormonalStudy, PatientOncologicStudy
from apps.nuclear_medicine.views import (
    HormonalStudyCreateView,
    HormonalStudyDeleteView,
    HormonalStudyDetailView,
    HormonalStudyUpdateView,
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
    # * Hormonal Study URLs
    path(
        "hormonal_study/list/",
        PaginationFilterView.as_view(
            model=PatientHormonalStudy,
            filterset_class=HormonalStudyFilter,
            extra_context={
                "crud_name": "Estudio hormonal",
                "crud_instance_name": "estudio hormonal",
                "add_url": "nuclear_medicine:hormonal_study_create",
                "detail_url": "nuclear_medicine:hormonal_study_detail",
                "edit_url": "nuclear_medicine:hormonal_study_update",
                "delete_url": "nuclear_medicine:hormonal_study_delete",
            },
        ),
        name="hormonal_study_list",
    ),
    path(
        "hormonal_study/create/",
        HormonalStudyCreateView.as_view(),
        name="hormonal_study_create",
    ),
    path(
        "hormonal_study/detail/<pk>/",
        HormonalStudyDetailView.as_view(),
        name="hormonal_study_detail",
    ),
    path(
        "hormonal_study/update/<pk>/",
        HormonalStudyUpdateView.as_view(),
        name="hormonal_study_update",
    ),
    path(
        "hormonal_study/delete/<pk>/",
        HormonalStudyDeleteView.as_view(),
        name="hormonal_study_delete",
    ),
]
