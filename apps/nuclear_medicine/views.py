from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.nuclear_medicine.forms import (
    HormonalStudyDetailForm,
    HormonalStudyForm,
    OncologicStudyDetailForm,
    OncologicStudyForm,
)
from apps.nuclear_medicine.models import PatientHormonalStudy, PatientOncologicStudy


# * OncologicStudy Views
class OncologicStudyCreateView(BaseCreateView):
    """View to handle oncologic study creation."""

    model = PatientOncologicStudy
    form_class = OncologicStudyForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    title = "Añadir estudio oncológico"


class OncologicStudyDetailView(BaseDetailView):
    """View to handle oncologic study details."""

    model = PatientOncologicStudy
    form_class = OncologicStudyDetailForm
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrada"
    title = "Detalles de estudio oncológico"


class OncologicStudyUpdateView(BaseUpdateView):
    """View to handle oncologic study edition."""

    model = PatientOncologicStudy
    form_class = OncologicStudyForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    title = "Editar estudio oncológico"


class OncologicStudyDeleteView(BaseDeleteView):
    """View to handle oncologic study delete."""

    model = PatientOncologicStudy
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    title = "Eliminar estudio oncológico"


# * HormonalStudy Views
class HormonalStudyCreateView(BaseCreateView):
    """View to handle hormonal study creation."""

    model = PatientHormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    title = "Añadir estudio hormonal"


class HormonalStudyDetailView(BaseDetailView):
    """View to handle hormonal study details."""

    model = PatientHormonalStudy
    form_class = HormonalStudyDetailForm
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrada"
    title = "Detalles de estudio hormonal"


class HormonalStudyUpdateView(BaseUpdateView):
    """View to handle hormonal study edition."""

    model = PatientHormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    title = "Editar estudio hormonal"


class HormonalStudyDeleteView(BaseDeleteView):
    """View to handle hormonal study delete."""

    model = PatientHormonalStudy
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    title = "Eliminar estudio hormonal"