from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)

from apps.radiotherapy.forms import (
    DosimetryPlanForm,
    EnergyForm,
    EquipmentForm,
    AccessoriesForm,
    RiskOrgansForm,
    PrescriptionForm,
    MedicalTurnForm,
    TACStudyForm,
)

from apps.radiotherapy.models import (
    DosimetryPlan,
    Energy,
    Equipment,
    Accessories,
    RiskOrgans,
    Prescription,
    MedicalTurn,
    TACStudy,
)

class DosimetryPlanCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = DosimetryPlan
    form_class = DosimetryPlanForm
    success_url = reverse_lazy("radiotherapy:DosimetryPlan_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "radiotherapy:DosimetryPlan_list"
    permission_required = "accounts.radiotherapy_manage"


class DosimetryPlanDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = DosimetryPlan
    form_class = DosimetryPlanForm
    cancel_url = "radiotherapy:DosimetryPlan_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class DosimetryPlanUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = DosimetryPlan
    form_class = DosimetryPlanForm
    success_url = reverse_lazy("radiotherapy:DosimetryPlan_list")
    success_message = "%(patient)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class DosimetryPlanDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = DosimetryPlan
    success_url = reverse_lazy("radiotherapy:DosimetryPlan_list")
    success_message = "%(patient)s eliminado correctamente."
    cancel_url = "radiotherapy:DosimetryPlan_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

######################################################################
class EnergyCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = Energy
    form_class = EnergyForm
    success_url = reverse_lazy("radiotherapy:Energy_list")
    success_message = "%(energy)s guardado correctamente."
    cancel_url = "radiotherapy:Energy_list"
    permission_required = "accounts.radiotherapy_manage"


class EnergyDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = Energy
    form_class = EnergyForm
    cancel_url = "radiotherapy:Energy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class EnergyUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = Energy
    form_class = EnergyForm
    success_url = reverse_lazy("radiotherapy:Energy_list")
    success_message = "%(energy)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class EnergyDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = Energy
    success_url = reverse_lazy("radiotherapy:Energy_list")
    success_message = "%(energy)s eliminado correctamente."
    cancel_url = "radiotherapy:Energy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

########################################################################

class EquipmentCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy("radiotherapy:Equipment_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:Equipment_list"
    permission_required = "accounts.radiotherapy_manage"


class EquipmentDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = Equipment
    form_class = EquipmentForm
    cancel_url = "radiotherapy:Equipment_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class EquipmentUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy("radiotherapy:Equipment_list")
    success_message = "%(name)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class EquipmentDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = Equipment
    success_url = reverse_lazy("radiotherapy:Equipment_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:Equipment_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

#################################################################################################

class AccessoriesCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = Accessories
    form_class = AccessoriesForm
    success_url = reverse_lazy("radiotherapy:Accessories_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:Accessories_list"
    permission_required = "accounts.radiotherapy_manage"


class AccessoriesDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = Accessories
    form_class = AccessoriesForm
    cancel_url = "radiotherapy:Accessories_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class AccessoriesUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = Accessories
    form_class = AccessoriesForm
    success_url = reverse_lazy("radiotherapy:Accessories_list")
    success_message = "%(name)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class AccessoriesDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = Accessories
    success_url = reverse_lazy("radiotherapy:Accessories_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:Accessories_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

class RiskOrgansCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = RiskOrgans
    form_class = RiskOrgansForm
    success_url = reverse_lazy("radiotherapy:RiskOrgans_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "radiotherapy:RiskOrgans_list"
    permission_required = "accounts.radiotherapy_manage"


class RiskOrgansDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = RiskOrgans
    form_class = RiskOrgansForm
    cancel_url = "radiotherapy:RiskOrgans_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class RiskOrgansUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = RiskOrgans
    form_class = RiskOrgansForm
    success_url = reverse_lazy("radiotherapy:RiskOrgans_list")
    success_message = "%(name)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class RiskOrgansDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = RiskOrgans
    success_url = reverse_lazy("radiotherapy:RiskOrgans_list")
    success_message = "%(name)s eliminado correctamente."
    cancel_url = "radiotherapy:RiskOrgans_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

class PrescriptionCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = Prescription
    form_class = PrescriptionForm
    success_url = reverse_lazy("radiotherapy:Prescription_list")
    success_message = "%(treatment_serie)s guardado correctamente."
    cancel_url = "radiotherapy:Prescription_list"
    permission_required = "accounts.radiotherapy_manage"


class PrescriptionDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = Prescription
    form_class = PrescriptionForm
    cancel_url = "radiotherapy:Prescription_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class PrescriptionUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = Prescription
    form_class = PrescriptionForm
    success_url = reverse_lazy("radiotherapy:Prescription_list")
    success_message = "%(treatment_serie)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class PrescriptionDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = Prescription
    success_url = reverse_lazy("radiotherapy:Prescription_list")
    success_message = "%(treatment_serie)s eliminado correctamente."
    cancel_url = "radiotherapy:Prescription_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

class MedicalTurnCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = MedicalTurn
    form_class = MedicalTurnForm
    success_url = reverse_lazy("radiotherapy:MedicalTurn_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "radiotherapy:MedicalTurn_list"
    permission_required = "accounts.radiotherapy_manage"


class MedicalTurnDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = MedicalTurn
    form_class = MedicalTurnForm
    cancel_url = "radiotherapy:MedicalTurn_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class MedicalTurnUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = MedicalTurn
    form_class = MedicalTurnForm
    success_url = reverse_lazy("radiotherapy:MedicalTurn_list")
    success_message = "%(patient)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class MedicalTurnDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = MedicalTurn
    success_url = reverse_lazy("radiotherapy:MedicalTurn_list")
    success_message = "%(patient)s eliminado correctamente."
    cancel_url = "radiotherapy:MedicalTurn_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"

class TACStudyCreateView(BaseCreateView):
    """View to handle Dosimetry Plan creation."""

    model = TACStudy
    form_class = TACStudyForm
    success_url = reverse_lazy("radiotherapy:TACStudy_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "radiotherapy:TACStudy_list"
    permission_required = "accounts.radiotherapy_manage"


class TACStudyDetailView(BaseDetailView):
    """View to handle Dosimetry Plan details."""

    model = TACStudy
    form_class = TACStudyForm
    cancel_url = "radiotherapy:TACStudy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class TACStudyUpdateView(BaseUpdateView):
    """View to handle Dosimetry Plan edition."""

    model = TACStudy
    form_class = TACStudyForm
    success_url = reverse_lazy("radiotherapy:TACStudy_list")
    success_message = "%(patient)s actualizado correctamente."
    cancel_url = "radiotherapy:radiotherapy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"


class TACStudyDeleteView(BaseDeleteView):
    """View to handle Dosimetry Plan delete."""

    model = TACStudy
    success_url = reverse_lazy("radiotherapy:TACStudy_list")
    success_message = "%(patient)s eliminado correctamente."
    cancel_url = "radiotherapy:TACStudy_list"
    object_not_found_error_message = "Plan de Dosimetría no encontrado"
    permission_required = "accounts.radiotherapy_manage"