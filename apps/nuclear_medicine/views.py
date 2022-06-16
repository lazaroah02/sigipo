from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.nuclear_medicine.forms import (
    GammagraphyForm,
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
    Gammagraphy,
    HormonalResult,
    HormonalStudy,
    IodineDetection,
    OncologicResult,
    OncologicStudy,
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
    permission_required = "cancer_registry_manage"


class OncologicStudyDetailView(BaseDetailView):
    """View to handle oncologic study details."""

    model = OncologicStudy
    form_class = OncologicStudyDetailForm
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrada"
    permission_required = "cancer_registry_view"


class OncologicStudyUpdateView(BaseUpdateView):
    """View to handle oncologic study edition."""

    model = OncologicStudy
    form_class = OncologicStudyForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    permission_required = "cancer_registry_manage"


class OncologicStudyDeleteView(BaseDeleteView):
    """View to handle oncologic study delete."""

    model = OncologicStudy
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_study_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    permission_required = "cancer_registry_manage"


# * HormonalStudy Views
class HormonalStudyCreateView(BaseCreateView):
    """View to handle hormonal study creation."""

    model = HormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    permission_required = "cancer_registry_manage"


class HormonalStudyDetailView(BaseDetailView):
    """View to handle hormonal study details."""

    model = HormonalStudy
    form_class = HormonalStudyDetailForm
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrada"
    permission_required = "cancer_registry_view"


class HormonalStudyUpdateView(BaseUpdateView):
    """View to handle hormonal study edition."""

    model = HormonalStudy
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    permission_required = "cancer_registry_view"


class HormonalStudyDeleteView(BaseDeleteView):
    """View to handle hormonal study delete."""

    model = HormonalStudy
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_study_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    permission_required = "cancer_registry_manage"


# * OncologicResult Views
class OncologicResultCreateView(BaseCreateView):
    """View to handle oncologic result creation."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    permission_required = "cancer_registry_manage"


class OncologicResultDetailView(BaseDetailView):
    """View to handle oncologic result details."""

    model = OncologicResult
    form_class = OncologicResultForm
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrada"
    permission_required = "cancer_registry_view"


class OncologicResultUpdateView(BaseUpdateView):
    """View to handle oncologic result edition."""

    model = OncologicResult
    form_class = OncologicResultForm
    success_url = reverse_lazy("nuclear_medicine:oncologic_study_list")
    success_message = "Estudio oncológico guardado correctamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Estudio oncológico no encontrado"
    permission_required = "cancer_registry_manage"


class OncologicResultDeleteView(BaseDeleteView):
    """View to handle oncologic result delete."""

    model = OncologicResult
    success_url = reverse_lazy("nuclear_medicine:oncologic_result_list")
    success_message = "Resultado oncológico eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:oncologic_result_list"
    object_not_found_error_message = "Resultado oncológico no encontrado"
    permission_required = "cancer_registry_manage"


# * HormonalResult Views
class HormonalResultCreateView(BaseCreateView):
    """View to handle hormonal result creation."""

    model = HormonalResult
    form_class = HormonalResultForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    permission_required = "cancer_registry_manage"


class HormonalResultDetailView(BaseDetailView):
    """View to handle hormonal result details."""

    model = HormonalResult
    form_class = HormonalResultForm
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrada"
    permission_required = "cancer_registry_view"


class HormonalResultUpdateView(BaseUpdateView):
    """View to handle hormonal result edition."""

    model = HormonalResult
    form_class = HormonalStudyForm
    success_url = reverse_lazy("nuclear_medicine:hormonal_study_list")
    success_message = "Estudio hormonal guardado correctamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Estudio hormonal no encontrado"
    permission_required = "cancer_registry_manage"


class HormonalResultDeleteView(BaseDeleteView):
    """View to handle hormonal result delete."""

    model = HormonalResult
    success_url = reverse_lazy("nuclear_medicine:hormonal_result_list")
    success_message = "Resultado hormonal eliminado satisfactoriamente."
    cancel_url = "nuclear_medicine:hormonal_result_list"
    object_not_found_error_message = "Resultado hormonal no encontrado"
    permission_required = "cancer_registry_manage"


# * IodineDetection Views
class IodineDetectionCreateView(BaseCreateView):
    """View to handle iodine detection creation."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    permission_required = "cancer_registry_manage"


class IodineDetectionDetailView(BaseDetailView):
    """View to handle iodine detection details."""

    model = IodineDetection
    form_class = IodineDetectionForm
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    permission_required = "cancer_registry_view"


class IodineDetectionUpdateView(BaseUpdateView):
    """View to handle iodine detection edition."""

    model = IodineDetection
    form_class = IodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo guardada correctamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    permission_required = "cancer_registry_manage"


class IodineDetectionDeleteView(BaseDeleteView):
    """View to handle iodine detection delete."""

    model = IodineDetection
    success_url = reverse_lazy("nuclear_medicine:iodine_detection_list")
    success_message = "Detección de yodo eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:iodine_detection_list"
    object_not_found_error_message = "Detección de yodo no encontrada"
    permission_required = "cancer_registry_manage"


# * SerialIodineDetection Views
class SerialIodineDetectionCreateView(BaseCreateView):
    """View to handle serial iodine detection creation."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    permission_required = "cancer_registry_manage"


class SerialIodineDetectionDetailView(BaseDetailView):
    """View to handle serial iodine detection details."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    permission_required = "cancer_registry_view"


class SerialIodineDetectionUpdateView(BaseUpdateView):
    """View to handle serial iodine detection edition."""

    model = SerialIodineDetection
    form_class = SerialIodineDetectionForm
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada guardada correctamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    permission_required = "cancer_registry_manage"


class SerialIodineDetectionDeleteView(BaseDeleteView):
    """View to handle serial iodine detection delete."""

    model = SerialIodineDetection
    success_url = reverse_lazy("nuclear_medicine:serial_iodine_detection_list")
    success_message = "Detección de yodo seriada eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:serial_iodine_detection_list"
    object_not_found_error_message = "Detección de yodo seriada no encontrada"
    permission_required = "cancer_registry_manage"


# * Gammagraphy Views
class GammagraphyCreateView(BaseCreateView):
    """View to handle gammagraphy creation."""

    model = Gammagraphy
    form_class = GammagraphyForm
    success_url = reverse_lazy("nuclear_medicine:gammagraphy_list")
    success_message = "Gammagrafía guardada correctamente."
    cancel_url = "nuclear_medicine:gammagraphy_list"
    permission_required = "cancer_registry_manage"


class GammagraphyDetailView(BaseDetailView):
    """View to handle gammagraphy details."""

    model = Gammagraphy
    form_class = GammagraphyForm
    cancel_url = "nuclear_medicine:gammagraphy_list"
    object_not_found_error_message = "Gammagrafía no encontrada"
    permission_required = "cancer_registry_view"


class GammagraphyUpdateView(BaseUpdateView):
    """View to handle gammagraphy edition."""

    model = Gammagraphy
    form_class = GammagraphyForm
    success_url = reverse_lazy("nuclear_medicine:gammagraphy_list")
    success_message = "Gammagrafía guardada correctamente."
    cancel_url = "nuclear_medicine:gammagraphy_list"
    object_not_found_error_message = "Gammagrafía no encontrada"
    permission_required = "cancer_registry_manage"


class GammagraphyDeleteView(BaseDeleteView):
    """View to handle gammagraphy delete."""

    model = Gammagraphy
    success_url = reverse_lazy("nuclear_medicine:gammagraphy_list")
    success_message = "Gammagrafía eliminada satisfactoriamente."
    cancel_url = "nuclear_medicine:gammagraphy_list"
    object_not_found_error_message = "Gammagrafía no encontrada"
    permission_required = "cancer_registry_manage"
