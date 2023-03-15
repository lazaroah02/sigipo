from django.urls import path

from apps.classifiers.filters import (
    MorphologyFilter,
    RadioIsotopeFilter,
    StudyFilter,
    TopographyFilter,
)
from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography
from apps.classifiers.views import (
    MorphologyCreateView,
    MorphologyDeleteView,
    MorphologyDetailView,
    MorphologyUpdateView,
    RadioIsotopeCreateView,
    RadioIsotopeDeleteView,
    RadioIsotopeDetailView,
    RadioIsotopeUpdateView,
    StudyCreateView,
    StudyDeleteView,
    StudyDetailView,
    StudyUpdateView,
    TopographyCreateView,
    TopographyDeleteView,
    TopographyDetailView,
    TopographyUpdateView,
)
from apps.core.views import PaginationFilterView, getUrl

app_name = "classifiers"
urlpatterns = [
    # * Morphology URLs
    path(
        "morphology/list/",
        PaginationFilterView.as_view(
            model=Morphology,
            filterset_class=MorphologyFilter,
            permission_required="accounts.cancer_registry_view",
        ),
        name="morphology_list",
    ),
    getUrl(MorphologyCreateView),
    getUrl(MorphologyDetailView),
    getUrl(MorphologyUpdateView),
    getUrl(MorphologyDeleteView),
    # * Topography URLs
    path(
        "topography/list/",
        PaginationFilterView.as_view(
            model=Topography,
            filterset_class=TopographyFilter,
            permission_required="accounts.cancer_registry_view",
        ),
        name="topography_list",
    ),
    getUrl(TopographyCreateView),
    getUrl(TopographyDetailView),
    getUrl(TopographyUpdateView),
    getUrl(TopographyDeleteView),
    # * Study URLs
    path(
        "study/list/",
        PaginationFilterView.as_view(
            model=Study,
            filterset_class=StudyFilter,
            permission_required="accounts.nuclear_medicine_view",
        ),
        name="study_list",
    ),
    getUrl(StudyCreateView),
    getUrl(StudyDetailView),
    getUrl(StudyUpdateView),
    getUrl(StudyDeleteView),
    # * RadioIsotope URLs
    path(
        "radioisotope/list/",
        PaginationFilterView.as_view(
            model=RadioIsotope,
            filterset_class=RadioIsotopeFilter,
            permission_required="accounts.nuclear_medicine_view",
        ),
        name="radioisotope_list",
    ),
    getUrl(RadioIsotopeCreateView),
    getUrl(RadioIsotopeDetailView),
    getUrl(RadioIsotopeUpdateView),
    getUrl(RadioIsotopeDeleteView),
]
