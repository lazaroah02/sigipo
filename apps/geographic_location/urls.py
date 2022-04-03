from django.urls import path
from django_filters.views import FilterView

from apps.geographic_location.models import Municipality, Province

app_name = "geographic_location"
urlpatterns = [
    path("province/list/", FilterView.as_view(model=Province), name="province_list"),
    path(
        "municipality/list/",
        FilterView.as_view(model=Municipality),
        name="municipality_list",
    ),
]
