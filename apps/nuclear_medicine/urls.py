from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
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
        ),
        name="oncologic_study_list",
    ),
    getUrl(OncologicStudyCreateView),
    getUrl(OncologicStudyDetailView),
    getUrl(OncologicStudyUpdateView),
    getUrl(OncologicStudyDeleteView),
    # * Hormonal Study URLs
    path(
        "hormonal_study/list/",
        PaginationFilterView.as_view(
            model=PatientHormonalStudy,
            filterset_class=HormonalStudyFilter,
        ),
        name="hormonal_study_list",
    ),
    getUrl(HormonalStudyCreateView),
    getUrl(HormonalStudyDetailView),
    getUrl(HormonalStudyUpdateView),
    getUrl(HormonalStudyDeleteView),
    # * Oncologic result URLs
    path(
        "oncologic_result/list/",
        PaginationFilterView.as_view(
            queryset=OncologicResult.objects.select_related(
                "oncologic_study__patient"
            ).all(),
            filterset_class=OncologicResultFilter,
        ),
        name="oncologic_result_list",
    ),
    getUrl(OncologicResultCreateView),
    getUrl(OncologicResultDetailView),
    getUrl(OncologicResultUpdateView),
    getUrl(OncologicResultDeleteView),
    # * Hormonal result URLs
    path(
        "hormonal_result/list/",
        PaginationFilterView.as_view(
            queryset=HormonalResult.objects.select_related(
                "hormonal_study__patient"
            ).all(),
            filterset_class=HormonalResultFilter,
        ),
        name="hormonal_result_list",
    ),
    getUrl(HormonalResultCreateView),
    getUrl(HormonalResultDetailView),
    getUrl(HormonalResultUpdateView),
    getUrl(HormonalResultDeleteView),
    # * IodineDetection result URLs
    path(
        "iodine_detection/list/",
        PaginationFilterView.as_view(
            model=IodineDetection,
            filterset_class=IodineDetectionFilter,
        ),
        name="iodine_detection_list",
    ),
    getUrl(IodineDetectionCreateView),
    getUrl(IodineDetectionDetailView),
    getUrl(IodineDetectionDeleteView),
    getUrl(IodineDetectionDeleteView),
    # * SerialIodineDetection result URLs
    path(
        "serial_iodine_detection/list/",
        PaginationFilterView.as_view(
            model=SerialIodineDetection,
            filterset_class=SerialIodineDetectionFilter,
        ),
        name="serial_iodine_detection_list",
    ),
    getUrl(SerialIodineDetectionCreateView),
    getUrl(SerialIodineDetectionDetailView),
    getUrl(SerialIodineDetectionUpdateView),
    getUrl(SerialIodineDetectionDeleteView),
]
