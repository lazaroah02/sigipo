from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.nuclear_medicine.forms import (
    HormonalResultForm,
    HormonalStudyDetailForm,
    HormonalStudyForm,
    IodineDetectionForm,
    OncologicResultForm,
    OncologicStudyDetailForm,
    OncologicStudyForm,
    SerialIodineDetectionForm,
)
from apps.nuclear_medicine.models import (
    HormonalResult,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
    PatientHormonalStudy,
    SerialIodineDetection,
)


# * OncologicStudy Views
class OncologicStudyCreateView(BaseCreateView):
    """View to handle oncologic study creation."""

    model = OncologicStudy
    form_class = OncologicStudyForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"


class OncologicStudyDetailView(BaseDetailView):
    """View to handle oncologic study details."""

    model = OncologicStudy
    form_class = OncologicStudyDetailForm
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrada"


class OncologicStudyUpdateView(BaseUpdateView):
    """View to handle oncologic study edition."""

    model = OncologicStudy
    form_class = OncologicStudyForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"


class OncologicStudyDeleteView(BaseDeleteView):
    """View to handle oncologic study delete."""

    model = OncologicStudy
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"


# * HormonalStudy Views
class HormonalStudyCreateView(BaseCreateView):
    """View to handle hormonal study creation."""

    model = PatientHormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"


class HormonalStudyDetailView(BaseDetailView):
    """View to handle hormonal study details."""

    model = PatientHormonalStudy
    form_class = HormonalStudyDetailForm
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrada"


class HormonalStudyUpdateView(BaseUpdateView):
    """View to handle hormonal study edition."""

    model = PatientHormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"


class HormonalStudyDeleteView(BaseDeleteView):
    """View to handle hormonal study delete."""

    model = PatientHormonalStudy
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"


# * OncologicResult Views
class OncologicResultCreateView(BaseCreateView):
    """View to handle oncologic result creation."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"


class OncologicResultDetailView(BaseDetailView):
    """View to handle oncologic result details."""

    model = OncologicResult
    form_class = OncologicResultForm
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrada"


class OncologicResultUpdateView(BaseUpdateView):
    """View to handle oncologic result edition."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"


class OncologicResultDeleteView(BaseDeleteView):
    """View to handle oncologic result delete."""

    model = OncologicResult
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrado"


# * HormonalResult Views
class HormonalResultCreateView(BaseCreateView):
    """View to handle hormonal result creation."""

    model = HormonalResult
    form_class = HormonalResultForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"


class HormonalResultDetailView(BaseDetailView):
    """View to handle hormonal result details."""

    model = HormonalResult
    form_class = HormonalResultForm
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrada"


class HormonalResultUpdateView(BaseUpdateView):
    """View to handle hormonal result edition."""

    model = HormonalResult
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"


class HormonalResultDeleteView(BaseDeleteView):
    """View to handle hormonal result delete."""

    model = HormonalResult
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrado"


# * IodineDetection Views
class IodineDetectionCreateView(BaseCreateView):
    """View to handle iodine detection creation."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"


class IodineDetectionDetailView(BaseDetailView):
    """View to handle iodine detection details."""

    model = IodineDetection
    form_class = IodineDetectionForm
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"


class IodineDetectionUpdateView(BaseUpdateView):
    """View to handle iodine detection edition."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"


class IodineDetectionDeleteView(BaseDeleteView):
    """View to handle iodine detection delete."""

    model = IodineDetection
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"


# * SerialIodineDetection Views
class SerialIodineDetectionCreateView(BaseCreateView):
    """View to handle serial iodine detection creation."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"


class SerialIodineDetectionDetailView(BaseDetailView):
    """View to handle serial iodine detection details."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"


class SerialIodineDetectionUpdateView(BaseUpdateView):
    """View to handle serial iodine detection edition."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"


class SerialIodineDetectionDeleteView(BaseDeleteView):
    """View to handle serial iodine detection delete."""

    model = SerialIodineDetection
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
