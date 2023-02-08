from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from apps.dashboard.views import Dashboard

app_name = "dashboard"

urlpatterns = [
    # * Dashboard URLs
    path("", RedirectView.as_view(url=reverse_lazy("dashboard:dashboard"))),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
