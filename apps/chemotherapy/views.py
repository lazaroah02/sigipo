# * Scheme Views


from django.urls import reverse_lazy

from apps.chemotherapy.forms import SchemeForm
from apps.chemotherapy.models import Scheme
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
