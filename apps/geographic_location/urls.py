from django.urls import path

from apps.core.views import PaginationFilterView
from apps.geographic_location.filters import ProvinceFilter
from apps.geographic_location.models import Municipality, Province
from apps.geographic_location.views import (
    ProvinceCreateView,
    ProvinceDeleteView,
    ProvinceDetailView,
    ProvinceUpdateView,
)

app_name = "geographic_location"
urlpatterns = [
    path(
        "province/list/",
        PaginationFilterView.as_view(
            model=Province,
            filterset_class=ProvinceFilter,
            extra_context={
                "crud_name": "Provincias",
                "add_url": "geographic_location:province_create",
                "crud_instance_name": "provincia",
                "edit_url": "geographic_location:province_update",
                "delete_url": "geographic_location:province_delete",
                "detail_url": "geographic_location:province_detail",
            },
        ),
        name="province_list",
    ),
    path(
        "municipality/list/",
        PaginationFilterView.as_view(model=Municipality),
        name="municipality_list",
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
]
