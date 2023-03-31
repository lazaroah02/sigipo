import io

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages import warning
from django.http import FileResponse, Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
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
from apps.patient.resources import PatientResource


# * Patient Views
class PatientCreateView(BaseCreateView):
    """View to handle patient creation."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"
    template_name = "patient/patient_create.html"
    permission_required = "patient:add_oncologic"


class PatientDetailView(BaseDetailView):
    """View to handle patient details."""

    model = Patient
    form_class = OncologicPatientForm
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    permission_required = "patient:view_oncologic"


class PatientUpdateView(BaseUpdateView):
    """View to handle patient edition."""

    model = Patient
    form_class = OncologicPatientForm
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s guardado correctamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    permission_required = "patient:change_oncologic"


class PatientDeleteView(BaseDeleteView):
    """View to handle patient delete."""

    model = Patient
    success_url = reverse_lazy("patient:oncologic_list")
    success_message = "%(first_name)s %(last_name)s eliminado satisfactoriamente."
    cancel_url = "patient:oncologic_list"
    object_not_found_error_message = "Paciente no encontrado"
    permission_required = "patient:delete_oncologic"


class PatientChangeStatus(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """View to change the status of a patient (Oncologic/No oncologic)."""

    template_name = "patient/change_status.html"
    permission_required = "patient.change_oncologic"

    def get_context_data(self, **kwargs):
        """Fills the context with the patient data or the form to search."""
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
        """Handles the POST request."""
        is_oncologic = Patient.objects.get(pk=kwargs["pk"]).is_oncologic
        Patient.objects.filter(pk=kwargs["pk"]).update(is_oncologic=(not is_oncologic))
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


@login_required
@permission_required("patient:view_oncologic", raise_exception=True)
@require_GET
def check_patient_created(request: HttpRequest, pk: str | int) -> JsonResponse:
    """Checks if the patient has been created."""
    return JsonResponse(
        data={"exist": Patient.objects.filter(identity_card=pk).exists()}, safe=False
    )


def patient_download_table(self, request: HttpRequest, *args, **kwargs) -> FileResponse:
    """Creates a xlsx file with the data of the table."""
    filterset_class = self.get_filterset_class()
    filterset = self.get_filterset(filterset_class)
    object_list = filterset.qs
    dataset = PatientResource().export(object_list)
    dataset.title = "Pacientes"
    buffer = io.BytesIO(dataset.xlsx)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="Datos de pacientes.xlsx")
