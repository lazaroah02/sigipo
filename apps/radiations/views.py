from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)

from apps.radiations.forms import (
    ExternalBeamTreatForm,
    ExternalBeamTreatDetailForm,
    InternalRadiationTreatmentForm,
    InternalRadiationTreatmentDetailForm,
    ExternalBeamRegForm,
    ExternalBeamRegDetailForm,
    InternalRadiationRegForm,
    InternalRadiationRegDetailForm
)

from apps.radiations.models import (
    ExternalBeamTreat,
    InternalRadiationTreatment,
    ExternalBeamReg,
    InternalRadiationReg
)


# * ExternalBeamTreat Views
class ExternalBeamTreatCreateView(BaseCreateView):
    """View to handle External Beam Treat creation."""

    model = ExternalBeamTreat
    form_class = ExternalBeamTreatForm
    success_url = reverse_lazy("radiations:external_beam_treat_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:external_beam_treat_list"
    permission_required = "accounts.radiations_manage"


class ExternalBeamTreatDetailView(BaseDetailView):
    """View to handle External Beam Treat details."""

    model = ExternalBeamTreat
    form_class = ExternalBeamTreatDetailForm
    cancel_url = "radiations:external_beam_treat_list"
    object_not_found_error_message = "Registro de tratamiento no encontrada"
    permission_required = "accounts.radiations_view"


class ExternalBeamTreatUpdateView(BaseUpdateView):
    """View to handle External Beam Treat edition."""

    model = ExternalBeamTreat
    form_class = ExternalBeamTreatForm
    success_url = reverse_lazy("radiations:external_beam_treat_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:external_beam_treat_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"


class ExternalBeamTreatDeleteView(BaseDeleteView):
    """View to handle External Beam Treat delete."""

    model = ExternalBeamTreat
    success_url = reverse_lazy("radiations:external_beam_treat_list")
    success_message = "Registro de tratamiento eliminado satisfactoriamente."
    cancel_url = "radiations:external_beam_treat_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"

#***********************Results External beam*******************************************************

class ExternalBeamRegCreateView(BaseCreateView):
    """View to handle External Beam Treat creation."""

    model = ExternalBeamReg
    form_class = ExternalBeamRegForm
    success_url = reverse_lazy("radiations:external_beam_reg_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:external_beam_reg_list"
    permission_required = "accounts.radiations_manage"


class ExternalBeamRegDetailView(BaseDetailView):
    """View to handle External Beam Treat details."""

    model = ExternalBeamReg
    form_class = ExternalBeamRegDetailForm
    cancel_url = "radiations:external_beam_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrada"
    permission_required = "accounts.radiations_view"


class ExternalBeamRegUpdateView(BaseUpdateView):
    """View to handle External Beam Treat edition."""

    model = ExternalBeamReg
    form_class = ExternalBeamRegForm
    success_url = reverse_lazy("radiations:external_beam_reg_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:external_beam_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"


class ExternalBeamRegDeleteView(BaseDeleteView):
    """View to handle External Beam Treat delete."""

    model = ExternalBeamReg
    success_url = reverse_lazy("radiations:external_beam_reg_list")
    success_message = "Registro de tratamiento eliminado satisfactoriamente."
    cancel_url = "radiations:external_beam_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"


########################################Internal Radiation###############################################


class InternalRadiationTreatCreateView(BaseCreateView):
    """View to handle Internal Radiation Treat creation."""

    model = InternalRadiationTreatment
    form_class = InternalRadiationTreatmentForm
    success_url = reverse_lazy("radiations:internal_radiation_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:internal_radiation_list"
    permission_required = "accounts.radiations_manage"


class InternalRadiationTreatDetailView(BaseDetailView):
    """View to handle Internal Radiation details."""

    model = InternalRadiationTreatment
    form_class = InternalRadiationTreatmentDetailForm
    cancel_url = "radiations:internal_radiation_list"
    object_not_found_error_message = "Registro de tratamiento no encontrada"
    permission_required = "accounts.radiations_view"


class InternalRadiationTreatUpdateView(BaseUpdateView):
    """View to handle Internal Radiation edition."""

    model = InternalRadiationTreatment
    form_class = InternalRadiationTreatmentForm
    success_url = reverse_lazy("radiations:internal_radiation_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:internal_radiation_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"


class InternalRadiationTreatDeleteView(BaseDeleteView):
    """View to handle Internal Radiation delete."""

    model = InternalRadiationTreatment
    success_url = reverse_lazy("radiations:internal_radiation_list")
    success_message = "Registro de tratamiento eliminado satisfactoriamente."
    cancel_url = "radiations:internal_radiation_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"

#****************************|Results Int Therapy**************************************

class InternalRadiationRegCreateView(BaseCreateView):
    """View to handle Internal Radiation Treat creation."""

    model = InternalRadiationReg
    form_class = InternalRadiationRegForm
    success_url = reverse_lazy("radiations:internal_radiation_reg_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:internal_radiation_reg_list"
    permission_required = "accounts.radiations_manage"


class InternalRadiationRegDetailView(BaseDetailView):
    """View to handle Internal Radiation details."""

    model = InternalRadiationReg
    form_class = InternalRadiationRegDetailForm
    cancel_url = "radiations:internal_radiation_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrada"
    permission_required = "accounts.radiations_view"


class InternalRadiationRegUpdateView(BaseUpdateView):
    """View to handle Internal Radiation edition."""

    model = InternalRadiationReg
    form_class = InternalRadiationRegForm
    success_url = reverse_lazy("radiations:internal_radiation_reg_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "radiations:internal_radiation_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"


class InternalRadiationRegDeleteView(BaseDeleteView):
    """View to handle Internal Radiation delete."""

    model = InternalRadiationReg
    success_url = reverse_lazy("radiations:internal_radiation_reg_list")
    success_message = "Registro de tratamiento eliminado satisfactoriamente."
    cancel_url = "radiations:internal_radiation_reg_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.radiations_manage"

