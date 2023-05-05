from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.geographic_location.filters import (
    LocationFilter,
    MunicipalityFilter,
    ProvinceFilter,
)
from apps.geographic_location.models import Location, Municipality, Province
from apps.geographic_location.views import (
    LocationCreateView,
    LocationDeleteView,
    LocationDetailView,
    LocationUpdateView,
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
        ),
        name="province_list",
    ),
    getUrl(ProvinceCreateView),
    getUrl(ProvinceDetailView),
    getUrl(ProvinceUpdateView),
    getUrl(ProvinceDeleteView),
    # * Municipality URLs
    path(
        "municipality/list/",
        PaginationFilterView.as_view(
            model=Municipality,
            filterset_class=MunicipalityFilter,
        ),
        name="municipality_list",
    ),
    getUrl(MunicipalityCreateView),
    getUrl(MunicipalityDetailView),
    getUrl(MunicipalityUpdateView),
    getUrl(MunicipalityDeleteView),
    # * Location URLs
    path(
        "location/list/",
        PaginationFilterView.as_view(
            model=Location,
            filterset_class=LocationFilter,
        ),
        name="location_list",
    ),
    getUrl(LocationCreateView),
    getUrl(LocationDetailView),
    getUrl(LocationUpdateView),
    getUrl(LocationDeleteView),
]
