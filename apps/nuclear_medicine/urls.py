from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.nuclear_medicine.filters import (
    GammagraphyFilter,
    HormonalResultFilter,
    HormonalStudyFilter,
    IodineDetectionFilter,
    OncologicResultFilter,
    OncologicStudyFilter,
    SerialIodineDetectionFilter,
)
from apps.nuclear_medicine.models import (
    Gammagraphy,
    HormonalResult,
    HormonalStudy,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    SerialIodineDetection,
)
from apps.nuclear_medicine.views import (
    GammagraphyCreateView,
    GammagraphyDeleteView,
    GammagraphyDetailView,
    GammagraphyUpdateView,
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
            model=OncologicStudy,
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
            model=HormonalStudy,
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
    getUrl(IodineDetectionUpdateView),
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
    # * Gammagraphy result URLs
    path(
        "gammagraphy/list/",
        PaginationFilterView.as_view(
            model=Gammagraphy,
            filterset_class=GammagraphyFilter,
        ),
        name="gammagraphy_list",
    ),
    getUrl(GammagraphyCreateView),
    getUrl(GammagraphyDetailView),
    getUrl(GammagraphyUpdateView),
    getUrl(GammagraphyDeleteView),
]
