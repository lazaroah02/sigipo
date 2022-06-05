# Create your views here.
from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.employee.forms import DoctorForm, GroupForm
from apps.employee.models import Doctor, Group


# * Group Views
class GroupCreateView(BaseCreateView):
    """View to handle Group creation."""

    model = Group
    form_class = GroupForm
    success_url = reverse_lazy("employee:group_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "employee:group_list"


class GroupDetailView(BaseDetailView):
    """View to handle Group details."""

    model = Group
    form_class = GroupForm
    cancel_url = "employee:group_list"
    object_not_found_error_message = "Grupo no encontrado"


class GroupUpdateView(BaseUpdateView):
    """View to handle Group edition."""

    model = Group
    form_class = GroupForm
    success_url = reverse_lazy("employee:group_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "employee:group_list"
    object_not_found_error_message = "Grupo no encontrado"


class GroupDeleteView(BaseDeleteView):
    """View to handle Group delete."""

    model = Group
    success_url = reverse_lazy("employee:group_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "employee:group_list"
    object_not_found_error_message = "Grupo no encontrado"


# * Doctor Views
class DoctorCreateView(BaseCreateView):
    """View to handle Doctor creation."""

    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("employee:doctor_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "employee:doctor_list"


class DoctorDetailView(BaseDetailView):
    """View to handle Doctor details."""

    model = Doctor
    form_class = DoctorForm
    cancel_url = "employee:doctor_list"
    object_not_found_error_message = "Doctor no encontrado"


class DoctorUpdateView(BaseUpdateView):
    """View to handle Doctor edition."""

    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("employee:doctor_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "employee:doctor_list"
    object_not_found_error_message = "Doctor no encontrado"


class DoctorDeleteView(BaseDeleteView):
    """View to handle Doctor delete."""

    model = Doctor
    success_url = reverse_lazy("employee:doctor_list")
    success_message = "%(first_name)s %(last_name)s eliminado satisfactoriamente."
    cancel_url = "employee:doctor_list"
    object_not_found_error_message = "Doctor no encontrado"
