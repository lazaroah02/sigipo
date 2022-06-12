from django.urls import reverse_lazy

from apps.cancer_registry.forms import NeoplasmForm
from apps.cancer_registry.models import Neoplasm
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)


# * Neoplasm Views
class NeoplasmCreateView(BaseCreateView):
    """View to handle neoplasm creation."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s guardada correctamente."
    cancel_url = "cancer_registry:neoplasm_list"
    title = "Añadir neoplasia"
    template_name = "cancer_registry/neoplasm_create.html"
    permission_required = "cancer_registry_manage"


class NeoplasmDetailView(BaseDetailView):
    """View to handle neoplasm details."""

    model = Neoplasm
    form_class = NeoplasmForm
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Detalles de neoplasia"
    template_name = "cancer_registry/neoplasm_detail.html"
    permission_required = "cancer_registry_view"


class NeoplasmUpdateView(BaseUpdateView):
    """View to handle neoplasm edition."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s guardada correctamente."
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Editar neoplasia"
    template_name = "cancer_registry/neoplasm_update.html"
    permission_required = "cancer_registry_manage"


class NeoplasmDeleteView(BaseDeleteView):
    """View to handle neoplasm delete."""

    model = Neoplasm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s eliminada satisfactoriamente."
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Eliminar neoplasia"
    permission_required = "cancer_registry_manage"
