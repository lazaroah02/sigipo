from django.urls import path

from apps.core.views import PaginationFilterView
from apps.geographic_location.filters import MunicipalityFilter, ProvinceFilter
from apps.geographic_location.models import Municipality, Province
from apps.geographic_location.views import (
    MunicipalityCreateView,
    MunicipalityDeleteView,
    MunicipalityDetailView,
    MunicipalityUpdateView,
    ProvinceCreateView,
    ProvinceDeleteView,
    ProvinceDetailView,
    ProvinceUpdateView,
)

app_name = "geographic_location"
urlpatterns = [
    # * Province URLs
    path(
        "province/list/",
        PaginationFilterView.as_view(
            model=Province,
            filterset_class=ProvinceFilter,
            extra_context={
                "crud_name": "Provincias",
                "crud_instance_name": "provincia",
                "add_url": "geographic_location:province_create",
                "detail_url": "geographic_location:province_detail",
                "edit_url": "geographic_location:province_update",
                "delete_url": "geographic_location:province_delete",
            },
        ),
        name="province_list",
    ),
    path(
        "province/create/",
        ProvinceCreateView.as_view(),
        name="province_create",
    ),
    path(
        "province/detail/<pk>/",
        ProvinceDetailView.as_view(),
        name="province_detail",
    ),
    path(
        "province/update/<pk>/",
        ProvinceUpdateView.as_view(),
        name="province_update",
    ),
    path(
        "province/delete/<pk>/",
        ProvinceDeleteView.as_view(),
        name="province_delete",
    ),
    # * Municipality URLs
    path(
        "municipality/list/",
        PaginationFilterView.as_view(
            model=Municipality,
            filterset_class=MunicipalityFilter,
            extra_context={
                "crud_name": "Municipios",
                "crud_instance_name": "municipio",
                "add_url": "geographic_location:municipality_create",
                "detail_url": "geographic_location:municipality_detail",
                "edit_url": "geographic_location:municipality_update",
                "delete_url": "geographic_location:municipality_delete",
            },
        ),
        name="municipality_list",
    ),
    path(
        "municipality/create/",
        MunicipalityCreateView.as_view(),
        name="municipality_create",
    ),
    path(
        "municipality/detail/<pk>/",
        MunicipalityDetailView.as_view(),
        name="municipality_detail",
    ),
    path(
        "municipality/update/<pk>/",
        MunicipalityUpdateView.as_view(),
        name="municipality_update",
    ),
    path(
        "municipality/delete/<pk>/",
        MunicipalityDeleteView.as_view(),
        name="municipality_delete",
    ),
]
