from django.urls import path

from apps.dashboard.views import Dashboard

app_name = "dashboard"

urlpatterns = [
    # * Dashboard URLs
    path("", Dashboard.as_view()),
    path("dashboard/", Dashboard.as_view()),
]
