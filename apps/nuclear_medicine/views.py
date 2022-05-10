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
    PatientHormonalStudy,
    PatientOncologicStudy,
    SerialIodineDetection,
)


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


# * OncologicResult Views
class OncologicResultCreateView(BaseCreateView):
    """View to handle oncologic result creation."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    title = "Añadir resultado oncológico"


class OncologicResultDetailView(BaseDetailView):
    """View to handle oncologic result details."""

    model = OncologicResult
    form_class = OncologicResultForm
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrada"
    title = "Detalles de resultado oncológico"


class OncologicResultUpdateView(BaseUpdateView):
    """View to handle oncologic result edition."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    title = "Editar estudio oncológico"


class OncologicResultDeleteView(BaseDeleteView):
    """View to handle oncologic result delete."""

    model = OncologicResult
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrado"
    title = "Eliminar resultado oncológico"


# * HormonalResult Views
class HormonalResultCreateView(BaseCreateView):
    """View to handle hormonal result creation."""

    model = HormonalResult
    form_class = HormonalResultForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    title = "Añadir resultado hormonal"


class HormonalResultDetailView(BaseDetailView):
    """View to handle hormonal result details."""

    model = HormonalResult
    form_class = HormonalResultForm
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrada"
    title = "Detalles de resultado hormonal"


class HormonalResultUpdateView(BaseUpdateView):
    """View to handle hormonal result edition."""

    model = HormonalResult
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    title = "Editar estudio hormonal"


class HormonalResultDeleteView(BaseDeleteView):
    """View to handle hormonal result delete."""

    model = HormonalResult
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrado"
    title = "Eliminar resultado hormonal"


# * IodineDetection Views
class IodineDetectionCreateView(BaseCreateView):
    """View to handle iodine detection creation."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    title = "Añadir detección de yodo"


class IodineDetectionDetailView(BaseDetailView):
    """View to handle iodine detection details."""

    model = IodineDetection
    form_class = IodineDetectionForm
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    title = "Detalles de detección de yodo"


class IodineDetectionUpdateView(BaseUpdateView):
    """View to handle iodine detection edition."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    title = "Editar detección de yodo"


class IodineDetectionDeleteView(BaseDeleteView):
    """View to handle iodine detection delete."""

    model = IodineDetection
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    title = "Eliminar detección de yodo"


# * SerialIodineDetection Views
class SerialIodineDetectionCreateView(BaseCreateView):
    """View to handle serial iodine detection creation."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    title = "Añadir detección de yodo seriada "


class SerialIodineDetectionDetailView(BaseDetailView):
    """View to handle serial iodine detection details."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    title = "Detalles de detección de yodo seriada "


class SerialIodineDetectionUpdateView(BaseUpdateView):
    """View to handle serial iodine detection edition."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    title = "Editar detección de yodo seriada"


class SerialIodineDetectionDeleteView(BaseDeleteView):
    """View to handle serial iodine detection delete."""

    model = SerialIodineDetection
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    title = "Eliminar detección de yodo seriada "
