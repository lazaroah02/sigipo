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
from apps.core.views import PaginationFilterView

app_name = "classifiers"
urlpatterns = [
    # * Morphology URLs
    path(
        "morphology/list/",
        PaginationFilterView.as_view(
            model=Morphology,
            filterset_class=MorphologyFilter,
            extra_context={
                "crud_name": "Morfologías",
                "crud_instance_name": "morfología",
                "add_url": "classifiers:morphology_create",
                "detail_url": "classifiers:morphology_detail",
                "edit_url": "classifiers:morphology_update",
                "delete_url": "classifiers:morphology_delete",
            },
        ),
        name="morphology_list",
    ),
    path(
        "morphology/create/",
        MorphologyCreateView.as_view(),
        name="morphology_create",
    ),
    path(
        "morphology/detail/<pk>/",
        MorphologyDetailView.as_view(),
        name="morphology_detail",
    ),
    path(
        "morphology/update/<pk>/",
        MorphologyUpdateView.as_view(),
        name="morphology_update",
    ),
    path(
        "morphology/delete/<pk>/",
        MorphologyDeleteView.as_view(),
        name="morphology_delete",
    ),
    # * Topography URLs
    path(
        "topography/list/",
        PaginationFilterView.as_view(
            model=Topography,
            filterset_class=TopographyFilter,
            extra_context={
                "crud_name": "Topografías",
                "crud_instance_name": "topografía",
                "add_url": "classifiers:topography_create",
                "detail_url": "classifiers:topography_detail",
                "edit_url": "classifiers:topography_update",
                "delete_url": "classifiers:topography_delete",
            },
        ),
        name="topography_list",
    ),
    path(
        "topography/create/",
        TopographyCreateView.as_view(),
        name="topography_create",
    ),
    path(
        "topography/detail/<pk>/",
        TopographyDetailView.as_view(),
        name="topography_detail",
    ),
    path(
        "topography/update/<pk>/",
        TopographyUpdateView.as_view(),
        name="topography_update",
    ),
    path(
        "topography/delete/<pk>/",
        TopographyDeleteView.as_view(),
        name="topography_delete",
    ),
]
