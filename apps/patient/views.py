from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.patient.forms import OncologicPatientForm
from apps.patient.models import Patient


# * Patient Views
class PatientCreateView(BaseCreateView):
    """View to handle patient creation."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"
    title = "Añadir paciente"


class PatientDetailView(BaseDetailView):
    """View to handle patient details."""

    model = Patient
    form_class = OncologicPatientForm
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    title = "Detalles de paciente"


class PatientUpdateView(BaseUpdateView):
    """View to handle patient edition."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    title = "Editar paciente"


class PatientDeleteView(BaseDeleteView):
    """View to handle patient delete."""

    model = Patient
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s eliminado satisfactoriamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    title = "Eliminar paciente"
