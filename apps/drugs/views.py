from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.drugs.forms import DrugForm
from apps.drugs.models import Drug


# * Drug Views
class DrugCreateView(BaseCreateView):
    """View to handle Drug creation."""

    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:drug_list"
    title = "Añadir fármaco"


class DrugDetailView(BaseDetailView):
    """View to handle Drug details."""

    model = Drug
    form_class = DrugForm
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrada"
    title = "Detalles de fármaco"


class DrugUpdateView(BaseUpdateView):
    """View to handle Drug edition."""

    model = Drug
    form_class = DrugForm
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrada"
    title = "Editar fármaco"


class DrugDeleteView(BaseDeleteView):
    """View to handle Drug delete."""

    model = Drug
    success_url = reverse_lazy("drugs:drug_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "drugs:drug_list"
    object_not_found_error_message = "Fármaco no encontrada"
    title = "Eliminar fármaco"
