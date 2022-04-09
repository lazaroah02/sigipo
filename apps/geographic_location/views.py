from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.geographic_location.forms import MunicipalityForm, ProvinceForm
from apps.geographic_location.models import Municipality, Province


# * Province Views
class ProvinceCreateView(BaseCreateView):
    """View to handle province creation."""

    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    title = "Añadir provincia"


class ProvinceDetailView(BaseDetailView):
    """View to handle province details."""

    model = Province
    form_class = ProvinceForm
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Detalles de provincia"


class ProvinceUpdateView(BaseUpdateView):
    """View to handle province edition."""

    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Editar provincia"


class ProvinceDeleteView(BaseDeleteView):
    """View to handle province delete."""

    model = Province
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Eliminar provincia"


# * Municipality View
class MunicipalityCreateView(BaseCreateView):
    """View to handle municipality creation."""

    model = Municipality
    form_class = MunicipalityForm
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:municipality_list"
    title = "Añadir municipio"


class MunicipalityDetailView(BaseDetailView):
    """View to handle municipality details."""

    model = Municipality
    form_class = MunicipalityForm
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"
    title = "Detalles de municipio"


class MunicipalityUpdateView(BaseUpdateView):
    """View to handle municipality edition."""

    model = Municipality
    form_class = MunicipalityForm
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"
    title = "Editar municipio"


class MunicipalityDeleteView(BaseDeleteView):
    """View to handle municipality delete."""

    model = Municipality
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"
    title = "Eliminar municipio"