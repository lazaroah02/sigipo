from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import warning
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.patient.forms import (
    NuclearMedicinePatientForm,
    OncologicPatientForm,
    PatientChangeStatusForm,
    PatientOncologicReadOnlyForm,
)
from apps.patient.models import Patient


# * Patient Views
class PatientCreateView(BaseCreateView):
    """View to handle patient creation."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"


class PatientDetailView(BaseDetailView):
    """View to handle patient details."""

    model = Patient
    form_class = OncologicPatientForm
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"


class PatientUpdateView(BaseUpdateView):
    """View to handle patient edition."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"


class PatientDeleteView(BaseDeleteView):
    """View to handle patient delete."""

    model = Patient
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s eliminado satisfactoriamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"


class PatientChangeStatus(LoginRequiredMixin, TemplateView):
    template_name = "patient/change_status.html"

    def get_context_data(self, **kwargs):
        if "pk" in kwargs:
            try:
                patient_object = Patient.objects.get(pk=kwargs["pk"])
            except Patient.DoesNotExist:
                raise Http404
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
                )
                detail_form = PatientOncologicReadOnlyForm(instance=patient_object)
            except Patient.DoesNotExist:
                patient_object = True
        return {"filter": filter_form, "object": patient_object, "form": detail_form}

    def post(self, request, *args, **kwargs):
        Patient.objects.filter(pk=kwargs["pk"]).update(is_oncologic=True)
        warning(request, "Estado de paciente actualizado.")
        return redirect("patient:oncologic_list")


# * Nuclear Medicine Patient Views
class NuclearMedicinePatientCreateView(PatientCreateView):
    """View to handle nuclear medicine patient creation."""

    model = Patient
    form_class = NuclearMedicinePatientForm
    success_url = reverse_lazy("patient:patient_list")
    cancel_url = "patient:patient_list"


class NuclearMedicinePatientDetailView(PatientDetailView):
    """View to handle nuclear medicine patient details."""

    form_class = NuclearMedicinePatientForm
    cancel_url = "patient:patient_list"


class NuclearMedicinePatientUpdateView(PatientUpdateView):
    """View to handle nuclear medicine patient edition."""

    model = Patient
    form_class = NuclearMedicinePatientForm
    success_url = reverse_lazy("patient:patient_list")
    cancel_url = "patient:patient_list"


class NuclearMedicinePatientDeleteView(BaseDeleteView):
    """View to handle nuclear medicine patient delete."""

    model = Patient
    success_url = reverse_lazy("patient:patient_list")
    cancel_url = "patient:patient_list"
