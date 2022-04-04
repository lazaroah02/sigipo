from django.urls import path

from apps.core.views import PaginationFilterView
from apps.geographic_location.filters import ProvinceFilter
from apps.geographic_location.models import Municipality, Province

app_name = "geographic_location"
urlpatterns = [
    path(
        "province/list/",
        PaginationFilterView.as_view(
            model=Province,
            filterset_class=ProvinceFilter,
            paginate_by=1,
            extra_context={"crud_name": "Provincias"},
        ),
        name="province_list",
    ),
    path(
        "municipality/list/",
        PaginationFilterView.as_view(model=Municipality),
        name="municipality_list",
    ),
]
