# * Scheme Views


from django.urls import reverse_lazy

from apps.chemotherapy.forms import MedicationForm, ProtocolForm, SchemeForm
from apps.chemotherapy.models import Medication, Protocol, Scheme
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)


# * Scheme Views
class SchemeCreateView(BaseCreateView):
    """View to handle Scheme creation."""

    model = Scheme
    form_class = SchemeForm
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "chemotherapy:scheme_list"
    permission_required = "chemotherapy_manage"


class SchemeDetailView(BaseDetailView):
    """View to handle Scheme details."""

    model = Scheme
    form_class = SchemeForm
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_view"


class SchemeUpdateView(BaseUpdateView):
    """View to handle Scheme edition."""

    model = Scheme
    form_class = SchemeForm
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_manage"


class SchemeDeleteView(BaseDeleteView):
    """View to handle Scheme delete."""

    model = Scheme
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_manage"


# * Protocol Views
class ProtocolCreateView(BaseCreateView):
    """View to handle Protocol creation."""

    model = Protocol
    form_class = ProtocolForm
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "chemotherapy:protocol_list"
    permission_required = "chemotherapy_manage"


class ProtocolDetailView(BaseDetailView):
    """View to handle Protocol details."""

    model = Protocol
    form_class = ProtocolForm
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_view"


class ProtocolUpdateView(BaseUpdateView):
    """View to handle Protocol edition."""

    model = Protocol
    form_class = ProtocolForm
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_manage"


class ProtocolDeleteView(BaseDeleteView):
    """View to handle Protocol delete."""

    model = Protocol
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s eliminado satisfactoriamente."
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_manage"


# * Medication Views


class MedicationCreateView(BaseCreateView):
    """View to handle Medication creation."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    permission_required = "chemotherapy_manage"


class MedicationDetailView(BaseUpdateView):
    """View to handle Medication details."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_view"


class MedicationUpdateView(BaseUpdateView):
    """View to handle Medication edition."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_manage"


class MedicationDeleteView(BaseDeleteView):
    """View to handle Medication delete."""

    model = Medication
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación eliminada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_manage"
