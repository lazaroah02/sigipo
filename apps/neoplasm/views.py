from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.neoplasm.forms import NeoplasmForm
from apps.neoplasm.models import Neoplasm


# * Neoplasm Views
class NeoplasmCreateView(BaseCreateView):
    """View to handle neoplasm creation."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("neoplasm:neoplasm_list")
    success_message = "%(primary_site__description)s guardada correctamente."
    cancel_url = "neoplasm:neoplasm_list"
    title = "Añadir neoplasia"


class NeoplasmDetailView(BaseDetailView):
    """View to handle neoplasm details."""

    model = Neoplasm
    form_class = NeoplasmForm
    cancel_url = "neoplasm:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Detalles de neoplasia"


class NeoplasmUpdateView(BaseUpdateView):
    """View to handle neoplasm edition."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("neoplasm:neoplasm_list")
    success_message = "%(primary_site__description)s guardada correctamente."
    cancel_url = "neoplasm:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Editar neoplasia"


class NeoplasmDeleteView(BaseDeleteView):
    """View to handle neoplasm delete."""

    model = Neoplasm
    success_url = reverse_lazy("neoplasm:neoplasm_list")
    success_message = "%(primary_site__description)s eliminada satisfactoriamente."
    cancel_url = "neoplasm:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Eliminar neoplasia"
