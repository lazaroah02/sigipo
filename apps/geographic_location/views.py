from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.geographic_location.forms import ProvinceForm
from apps.geographic_location.models import Province


class ProvinceCreateView(BaseCreateView):
    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    title = "Añadir provincia"


class ProvinceDetailView(BaseDetailView):
    model = Province
    form_class = ProvinceForm
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Detalles de provincia"


class ProvinceUpdateView(BaseUpdateView):
    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Editar provincia"


class ProvinceDeleteView(BaseDeleteView):
    model = Province
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"
    title = "Eliminar provincia"
