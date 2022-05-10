from django.urls import path

from apps.core.views import PaginationFilterView
from apps.nuclear_medicine.filters import (
    HormonalResultFilter,
    HormonalStudyFilter,
    IodineDetectionFilter,
    OncologicResultFilter,
    OncologicStudyFilter,
    SerialIodineDetectionFilter,
)
from apps.nuclear_medicine.models import (
    HormonalResult,
    IodineDetection,
    OncologicResult,
    PatientHormonalStudy,
    PatientOncologicStudy,
    SerialIodineDetection,
)
from apps.nuclear_medicine.views import (
    HormonalResultCreateView,
    HormonalResultDeleteView,
    HormonalResultDetailView,
    HormonalResultUpdateView,
    HormonalStudyCreateView,
    HormonalStudyDeleteView,
    HormonalStudyDetailView,
    HormonalStudyUpdateView,
    IodineDetectionCreateView,
    IodineDetectionDeleteView,
    IodineDetectionDetailView,
    IodineDetectionUpdateView,
    OncologicResultCreateView,
    OncologicResultDeleteView,
    OncologicResultDetailView,
    OncologicResultUpdateView,
    OncologicStudyCreateView,
    OncologicStudyDeleteView,
    OncologicStudyDetailView,
    OncologicStudyUpdateView,
    SerialIodineDetectionCreateView,
    SerialIodineDetectionDeleteView,
    SerialIodineDetectionDetailView,
    SerialIodineDetectionUpdateView,
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
    # * Oncologic result URLs
    path(
        "oncologic_result/list/",
        PaginationFilterView.as_view(
            queryset=OncologicResult.objects.select_related(
                "oncologic_study__patient"
            ).all(),
            filterset_class=OncologicResultFilter,
            extra_context={
                "crud_name": "Resultado oncológico",
                "crud_instance_name": "resultado oncológico",
                "add_url": "nuclear_medicine:oncologic_result_create",
                "detail_url": "nuclear_medicine:oncologic_result_detail",
                "edit_url": "nuclear_medicine:oncologic_result_update",
                "delete_url": "nuclear_medicine:oncologic_result_delete",
            },
        ),
        name="oncologic_result_list",
    ),
    path(
        "oncologic_result/create/",
        OncologicResultCreateView.as_view(),
        name="oncologic_result_create",
    ),
    path(
        "oncologic_result/detail/<pk>/",
        OncologicResultDetailView.as_view(),
        name="oncologic_result_detail",
    ),
    path(
        "oncologic_result/update/<pk>/",
        OncologicResultUpdateView.as_view(),
        name="oncologic_result_update",
    ),
    path(
        "oncologic_result/delete/<pk>/",
        OncologicResultDeleteView.as_view(),
        name="oncologic_result_delete",
    ),
    # * Hormonal result URLs
    path(
        "hormonal_result/list/",
        PaginationFilterView.as_view(
            queryset=HormonalResult.objects.select_related(
                "hormonal_study__patient"
            ).all(),
            filterset_class=HormonalResultFilter,
            extra_context={
                "crud_name": "Resultado hormonal",
                "crud_instance_name": "resultado hormonal",
                "add_url": "nuclear_medicine:hormonal_result_create",
                "detail_url": "nuclear_medicine:hormonal_result_detail",
                "edit_url": "nuclear_medicine:hormonal_result_update",
                "delete_url": "nuclear_medicine:hormonal_result_delete",
            },
        ),
        name="hormonal_result_list",
    ),
    path(
        "hormonal_result/create/",
        HormonalResultCreateView.as_view(),
        name="hormonal_result_create",
    ),
    path(
        "hormonal_result/detail/<pk>/",
        HormonalResultDetailView.as_view(),
        name="hormonal_result_detail",
    ),
    path(
        "hormonal_result/update/<pk>/",
        HormonalResultUpdateView.as_view(),
        name="hormonal_result_update",
    ),
    path(
        "hormonal_result/delete/<pk>/",
        HormonalResultDeleteView.as_view(),
        name="hormonal_result_delete",
    ),
    # * IodineDetection result URLs
    path(
        "iodine_detection/list/",
        PaginationFilterView.as_view(
            queryset=IodineDetection.objects.all(),
            filterset_class=IodineDetectionFilter,
            extra_context={
                "crud_name": "Detección de yodo",
                "crud_instance_name": "detección de yodo",
                "add_url": "nuclear_medicine:iodine_detection_create",
                "detail_url": "nuclear_medicine:iodine_detection_detail",
                "edit_url": "nuclear_medicine:iodine_detection_update",
                "delete_url": "nuclear_medicine:iodine_detection_delete",
            },
        ),
        name="iodine_detection_list",
    ),
    path(
        "iodine_detection/create/",
        IodineDetectionCreateView.as_view(),
        name="iodine_detection_create",
    ),
    path(
        "iodine_detection/detail/<pk>/",
        IodineDetectionDetailView.as_view(),
        name="iodine_detection_detail",
    ),
    path(
        "iodine_detection/update/<pk>/",
        IodineDetectionUpdateView.as_view(),
        name="iodine_detection_update",
    ),
    path(
        "iodine_detection/delete/<pk>/",
        IodineDetectionDeleteView.as_view(),
        name="iodine_detection_delete",
    ),
    # * SerialIodineDetection result URLs
    path(
        "serial_iodine_detection/list/",
        PaginationFilterView.as_view(
            queryset=SerialIodineDetection.objects.all(),
            filterset_class=SerialIodineDetectionFilter,
            extra_context={
                "crud_name": "Detección de yodo seriada",
                "crud_instance_name": "detección de yodo seriada",
                "add_url": "nuclear_medicine:serial_iodine_detection_create",
                "detail_url": "nuclear_medicine:serial_iodine_detection_detail",
                "edit_url": "nuclear_medicine:serial_iodine_detection_update",
                "delete_url": "nuclear_medicine:serial_iodine_detection_delete",
            },
        ),
        name="serial_iodine_detection_list",
    ),
    path(
        "serial_iodine_detection/create/",
        SerialIodineDetectionCreateView.as_view(),
        name="serial_iodine_detection_create",
    ),
    path(
        "serial_iodine_detection/detail/<pk>/",
        SerialIodineDetectionDetailView.as_view(),
        name="serial_iodine_detection_detail",
    ),
    path(
        "serial_iodine_detection/update/<pk>/",
        SerialIodineDetectionUpdateView.as_view(),
        name="serial_iodine_detection_update",
    ),
    path(
        "serial_iodine_detection/delete/<pk>/",
        SerialIodineDetectionDeleteView.as_view(),
        name="serial_iodine_detection_delete",
    ),
]
