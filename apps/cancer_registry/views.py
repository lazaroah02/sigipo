from django.urls import reverse_lazy

from apps.cancer_registry.forms import NeoplasmForm, TNMForm
from apps.cancer_registry.models import TNM, Neoplasm
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


class NeoplasmDetailView(BaseDetailView):
    """View to handle neoplasm details."""

    model = Neoplasm
    form_class = NeoplasmForm
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Detalles de neoplasia"
    template_name = "cancer_registry/neoplasm_detail.html"


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


class NeoplasmDeleteView(BaseDeleteView):
    """View to handle neoplasm delete."""

    model = Neoplasm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s eliminada satisfactoriamente."
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Eliminar neoplasia"


# * TNM Views
class TNMCreateView(BaseCreateView):
    """View to handle tnm creation."""

    model = TNM
    form_class = TNMForm
    success_url = reverse_lazy("cancer_registry:tnm_list")
    success_message = (
        "%(patient)s %(tumor)s %(nodule)s %(metastasis)s guardado correctamente."
    )
    cancel_url = "cancer_registry:tnm_list"
    title = "Añadir TNM"


class TNMDetailView(BaseDetailView):
    """View to handle tnm details."""

    model = TNM
    form_class = TNMForm
    cancel_url = "cancer_registry:tnm_list"
    object_not_found_error_message = "TNM no encontrada"
    title = "Detalles de TNM"


class TNMUpdateView(BaseUpdateView):
    """View to handle tnm edition."""

    model = TNM
    form_class = TNMForm
    success_url = reverse_lazy("cancer_registry:tnm_list")
    success_message = (
        "%(patient)s %(tumor)s %(nodule)s %(metastasis)s guardado correctamente."
    )
    cancel_url = "cancer_registry:tnm_list"
    object_not_found_error_message = "TNM no encontrada"
    title = "Editar TNM"


class TNMDeleteView(BaseDeleteView):
    """View to handle tnm delete."""

    model = TNM
    success_url = reverse_lazy("cancer_registry:tnm_list")
    success_message = (
        "%(tumor)s %(nodule)s %(metastasis)s eliminada satisfactoriamente."
    )
    cancel_url = "cancer_registry:tnm_list"
    object_not_found_error_message = "TNM no encontrada"
    title = "Eliminar TNM"
