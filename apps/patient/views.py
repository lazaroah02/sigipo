from http.client import NOT_FOUND

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import warning
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.cancer_registry.models import Neoplasm
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.patient.forms import (
    OncologicPatientForm,
    PatientChangeStatusForm,
    PatientOncologicReadOnlyForm,
)
from apps.patient.models import Patient


# * Patient Views
class PatientCreateView(BaseCreateView):
    """View to handle patient creation."""

    model = Neoplasm
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


class PatientChangeStatus(LoginRequiredMixin, TemplateView):
    template_name = "patient/change_status.html"

    def get_context_data(self, **kwargs):
        if "pk" in kwargs:
            try:
                patient_object = Patient.objects.get(pk=kwargs["pk"])
            except Patient.DoesNotExist:
                raise NOT_FOUND
            return {"confirmation": True, "object": patient_object}
        patient_object = None
        filter_form = PatientChangeStatusForm(self.request.GET)
        detail_form = None
        if filter_form.is_valid():
            filter_form.full_clean()
            try:
                data = filter_form.cleaned_data
                patient_object = Patient.objects.get(
                    identity_card=data["identity_card"],
                    medical_record=data["medical_record"],
                )
                detail_form = PatientOncologicReadOnlyForm(instance=patient_object)
            except Patient.DoesNotExist:
                patient_object = True
        return {"filter": filter_form, "object": patient_object, "form": detail_form}

    def post(self, request, *args, **kwargs):
        Patient.objects.filter(pk=kwargs["pk"]).update(is_oncologic=True)
        warning(request, "Estado de paciente actualizado.")
        return redirect("patient:oncologic_list")
