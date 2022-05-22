from django.urls import reverse_lazy

from apps.classifiers.forms import (
    MorphologyForm,
    RadioIsotopeForm,
    StudyForm,
    TopographyForm,
)
from apps.classifiers.models import Morphology, RadioIsotope, Study, Topography
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)


# * Morphology Views
class MorphologyCreateView(BaseCreateView):
    """View to handle morphology creation."""

    model = Morphology
    form_class = MorphologyForm
    success_url = reverse_lazy("classifiers:morphology_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:morphology_list"


class MorphologyDetailView(BaseDetailView):
    """View to handle morphology details."""

    model = Morphology
    form_class = MorphologyForm
    cancel_url = "classifiers:morphology_list"
    object_not_found_error_message = "Morfología no encontrada"


class MorphologyUpdateView(BaseUpdateView):
    """View to handle morphology edition."""

    model = Morphology
    form_class = MorphologyForm
    success_url = reverse_lazy("classifiers:morphology_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:morphology_list"
    object_not_found_error_message = "Morfología no encontrado"


class MorphologyDeleteView(BaseDeleteView):
    """View to handle morphology delete."""

    model = Morphology
    success_url = reverse_lazy("classifiers:morphology_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:morphology_list"
    object_not_found_error_message = "Morfología no encontrado"


# * Topography Views
class TopographyCreateView(BaseCreateView):
    """View to handle topography creation."""

    model = Topography
    form_class = TopographyForm
    success_url = reverse_lazy("classifiers:topography_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:topography_list"


class TopographyDetailView(BaseDetailView):
    """View to handle topography details."""

    model = Topography
    form_class = TopographyForm
    cancel_url = "classifiers:topography_list"
    object_not_found_error_message = "Topografía no encontrada"


class TopographyUpdateView(BaseUpdateView):
    """View to handle topography edition."""

    model = Topography
    form_class = TopographyForm
    success_url = reverse_lazy("classifiers:topography_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:topography_list"
    object_not_found_error_message = "Topografía no encontrado"


class TopographyDeleteView(BaseDeleteView):
    """View to handle topography delete."""

    model = Topography
    success_url = reverse_lazy("classifiers:topography_list")
    success_message = "%(description)s guardada correctamente."
    cancel_url = "classifiers:topography_list"
    object_not_found_error_message = "Topografía no encontrado"


# * Study Views
class StudyCreateView(BaseCreateView):
    """View to handle study creation."""

    model = Study
    form_class = StudyForm
    success_url = reverse_lazy("classifiers:study_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:study_list"


class StudyDetailView(BaseDetailView):
    """View to handle study details."""

    model = Study
    form_class = StudyForm
    cancel_url = "classifiers:study_list"
    object_not_found_error_message = "Estudio no encontrada"


class StudyUpdateView(BaseUpdateView):
    """View to handle study edition."""

    model = Study
    form_class = StudyForm
    success_url = reverse_lazy("classifiers:study_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:study_list"
    object_not_found_error_message = "Estudio no encontrado"


class StudyDeleteView(BaseDeleteView):
    """View to handle study delete."""

    model = Study
    success_url = reverse_lazy("classifiers:study_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:study_list"
    object_not_found_error_message = "Estudio no encontrado"


# * RadioIsotope Views
class RadioIsotopeCreateView(BaseCreateView):
    """View to handle study creation."""

    model = RadioIsotope
    form_class = RadioIsotopeForm
    success_url = reverse_lazy("classifiers:radioisotope_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:radioisotope_list"


class RadioIsotopeDetailView(BaseDetailView):
    """View to handle study details."""

    model = RadioIsotope
    form_class = RadioIsotopeForm
    cancel_url = "classifiers:radioisotope_list"
    object_not_found_error_message = "Radio isótopo no encontrada"


class RadioIsotopeUpdateView(BaseUpdateView):
    """View to handle study edition."""

    model = RadioIsotope
    form_class = RadioIsotopeForm
    success_url = reverse_lazy("classifiers:radioisotope_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:radioisotope_list"
    object_not_found_error_message = "Radio isótopo no encontrado"


class RadioIsotopeDeleteView(BaseDeleteView):
    """View to handle study delete."""

    model = RadioIsotope
    success_url = reverse_lazy("classifiers:radioisotope_list")
    success_message = "%(name)s guardada correctamente."
    cancel_url = "classifiers:radioisotope_list"
    object_not_found_error_message = "Radio isótopo no encontrado"
