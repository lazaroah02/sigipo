from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)

from apps.pathological_anatomy.forms import (
    PathologyForm
)

from apps.pathological_anatomy.models import (
    Pathology
)


class PathologyCreateView(BaseCreateView):
    """View to handle Pathology creation."""

    model = Pathology
    form_class = PathologyForm
    success_url = reverse_lazy("pathological_anatomy:pathology_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "pathological_anatomy:pathology_list"
    permission_required = "accounts.pathological_anatomy_manage"


class PathologyDetailView(BaseDetailView):
    """View to handle Pathology details."""

    model = Pathology
    form_class = PathologyForm
    cancel_url = "pathological_anatomy:pathology_list"
    object_not_found_error_message = "Registro de tratamiento no encontrada"
    permission_required = "accounts.pathological_anatomy_view"


class PathologyUpdateView(BaseUpdateView):
    """View to handle Pathology edition."""

    model = Pathology
    form_class = PathologyForm
    success_url = reverse_lazy("pathological_anatomy:pathology_list")
    success_message = "Registro de tratamiento guardado correctamente."
    cancel_url = "pathological_anatomy:pathology_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.pathological_anatomy_manage"


class PathologyDeleteView(BaseDeleteView):
    """View to handle Pathology delete."""

    model = Pathology
    success_url = reverse_lazy("pathological_anatomy:pathology_list")
    success_message = "Registro de tratamiento eliminado satisfactoriamente."
    cancel_url = "pathological_anatomy:pathology_list"
    object_not_found_error_message = "Registro de tratamiento no encontrado"
    permission_required = "accounts.pathological_anatomy_manage"
