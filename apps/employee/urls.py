from django.urls import path

from apps.core.views import PaginationFilterView, getUrl
from apps.employee.filters import DoctorFilter, GroupFilter
from apps.employee.models import Doctor, Group
from apps.employee.views import (
    DoctorCreateView,
    DoctorDeleteView,
    DoctorDetailView,
    DoctorUpdateView,
    GroupCreateView,
    GroupDeleteView,
    GroupDetailView,
    GroupUpdateView,
)

app_name = "employee"
urlpatterns = [
    # * Group URLs
    path(
        "group/list/",
        PaginationFilterView.as_view(
            model=Group,
            filterset_class=GroupFilter,
            permission_required="employee_view",
        ),
        name="group_list",
    ),
    getUrl(GroupCreateView),
    getUrl(GroupDetailView),
    getUrl(GroupUpdateView),
    getUrl(GroupDeleteView),
    # * Doctor URLs
    path(
        "doctor/list/",
        PaginationFilterView.as_view(
            model=Doctor,
            filterset_class=DoctorFilter,
            permission_required="employee_view",
        ),
        name="doctor_list",
    ),
    getUrl(DoctorCreateView),
    getUrl(DoctorDetailView),
    getUrl(DoctorUpdateView),
    getUrl(DoctorDeleteView),
]
