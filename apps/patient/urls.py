from django.urls import path

from apps.core.views import PaginationFilterView
from apps.patient.filters import PatientFilter
from apps.patient.models import Patient
from apps.patient.views import (
    PatientCreateView,
    PatientDeleteView,
    PatientDetailView,
    PatientUpdateView,
)

app_name = "patient"

urlpatterns = [
    # * Patient URLs
    path(
        "oncologic/list/",
        PaginationFilterView.as_view(
            model=Patient,
            filterset_class=PatientFilter,
            extra_context={
                "crud_name": "Pacientes",
                "crud_instance_name": "provincia",
                "add_url": "patient:oncologic_create",
                "detail_url": "patient:oncologic_detail",
                "edit_url": "patient:oncologic_update",
                "delete_url": "patient:oncologic_delete",
            },
            queryset=Patient.objects.filter(is_oncologic=True).select_related(
                "residence_municipality", "born_municipality"
            ),
        ),
        name="oncologic_list",
    ),
    path(
        "oncologic/create/",
        PatientCreateView.as_view(),
        name="oncologic_create",
    ),
    path(
        "oncologic/detail/<pk>/",
        PatientDetailView.as_view(),
        name="oncologic_detail",
    ),
    path(
        "oncologic/update/<pk>/",
        PatientUpdateView.as_view(),
        name="oncologic_update",
    ),
    path(
        "oncologic/delete/<pk>/",
        PatientDeleteView.as_view(),
        name="oncologic_delete",
    ),
]
