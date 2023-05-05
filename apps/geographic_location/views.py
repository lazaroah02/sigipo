from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.geographic_location.forms import LocationForm, MunicipalityForm, ProvinceForm
from apps.geographic_location.models import Location, Municipality, Province


# * Province Views
class ProvinceCreateView(BaseCreateView):
    """View to handle province creation."""

    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"


class ProvinceDetailView(BaseDetailView):
    """View to handle province details."""

    model = Province
    form_class = ProvinceForm
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"


class ProvinceUpdateView(BaseUpdateView):
    """View to handle province edition."""

    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"


class ProvinceDeleteView(BaseDeleteView):
    """View to handle province delete."""

    model = Province
    success_url = reverse_lazy("geographic_location:province_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:province_list"
    object_not_found_error_message = "Provincia no encontrada"


# * Municipality View
class MunicipalityCreateView(BaseCreateView):
    """View to handle municipality creation."""

    model = Municipality
    form_class = MunicipalityForm
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:municipality_list"


class MunicipalityDetailView(BaseDetailView):
    """View to handle municipality details."""

    model = Municipality
    form_class = MunicipalityForm
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"


class MunicipalityUpdateView(BaseUpdateView):
    """View to handle municipality edition."""

    model = Municipality
    form_class = MunicipalityForm
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"


class MunicipalityDeleteView(BaseDeleteView):
    """View to handle municipality delete."""

    model = Municipality
    success_url = reverse_lazy("geographic_location:municipality_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:municipality_list"
    object_not_found_error_message = "Municipio no encontrada"


# * Location View
class LocationCreateView(BaseCreateView):
    """View to handle Location creation."""

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("geographic_location:location_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:location_list"


class LocationDetailView(BaseDetailView):
    """View to handle Location details."""

    model = Location
    form_class = LocationForm
    cancel_url = "geographic_location:location_list"
    object_not_found_error_message = "Localidad no encontrada"


class LocationUpdateView(BaseUpdateView):
    """View to handle Location edition."""

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("geographic_location:location_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "geographic_location:location_list"
    object_not_found_error_message = "Localidad no encontrada no encontrada"


class LocationDeleteView(BaseDeleteView):
    """View to handle Location delete."""

    model = Location
    success_url = reverse_lazy("geographic_location:location_list")
    success_message = "%(name)s eliminada satisfactoriamente."
    cancel_url = "geographic_location:location_list"
    object_not_found_error_message = "Localidad no encontrada no encontrada"
