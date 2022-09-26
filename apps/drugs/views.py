from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.drugs.forms import DrugForm, NuclearMedicineDrugForm
from apps.drugs.models import Drug, NuclearMedicineDrug


# * NuclearMedicineDrug Views
class NuclearMedicineDrugCreateView(BaseCreateView):
    """View to handle NuclearMedicineDrug creation."""

    model = NuclearMedicineDrug
    form_class = NuclearMedicineDrugForm
    success_url = reverse_lazy("drugs:nuclearmedicinedrug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:nuclearmedicinedrug_list"
    permission_required = "accounts.drug_manage"


class NuclearMedicineDrugDetailView(BaseDetailView):
    """View to handle Drug details."""

    model = NuclearMedicineDrug
    form_class = NuclearMedicineDrugForm
    cancel_url = "drugs:nuclearmedicinedrug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_view"


class NuclearMedicineDrugUpdateView(BaseUpdateView):
    """View to handle NuclearMedicineDrug edition."""

    model = NuclearMedicineDrug
    form_class = NuclearMedicineDrugForm
    success_url = reverse_lazy("drugs:nuclearmedicinedrug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:nuclearmedicinedrug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_manage"


class NuclearMedicineDrugDeleteView(BaseDeleteView):
    """View to handle NuclearMedicineDrug delete."""

    model = NuclearMedicineDrug
    success_url = reverse_lazy("drugs:nuclearmedicinedrug_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "drugs:nuclearmedicinedrug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_manage"


# * Drug Views


class DrugCreateView(BaseCreateView):
    """View to handle NuclearMedicineDrug creation."""

    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:drug_list"
    permission_required = "accounts.drug_manage"


class DrugDetailView(BaseDetailView):
    """View to handle Drug details."""

    model = Drug
    form_class = DrugForm
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_view"


class DrugUpdateView(BaseUpdateView):
    """View to handle NuclearMedicineDrug edition."""

    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_manage"


class DrugDeleteView(BaseDeleteView):
    """View to handle Drug delete."""

    model = Drug
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrado"
    permission_required = "accounts.drug_manage"
