from django.urls import path

from apps.classifiers.filters import MorphologyFilter, TopographyFilter
from apps.classifiers.models import Morphology, Topography
from apps.classifiers.views import (
    MorphologyCreateView,
    MorphologyDeleteView,
    MorphologyDetailView,
    MorphologyUpdateView,
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
        ),
        name="topography_list",
    ),
    getUrl(TopographyCreateView),
    getUrl(TopographyDetailView),
    getUrl(TopographyUpdateView),
    getUrl(TopographyDeleteView),
]
