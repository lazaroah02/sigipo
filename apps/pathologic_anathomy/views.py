from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.pathologic_anathomy.forms import BiopsyRequestForm
from apps.pathologic_anathomy.forms_biopsy_diagnostic.form_head import HeadBiopsyForm
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic.model_head import Head


# Create your views here.
class BiopsyRequestCreateView(BaseCreateView):
    """View to handle BiopsyOrder view."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"


class BiopsyRequestDetailView(BaseDetailView):
    """View to handle BiopsyOrder details."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Orden de biopsia no encontrada"


class BiopsyRequestUpdateView(BaseUpdateView):
    """View to handle BiopsyOrder edition."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"


class BiopsyRequestDeleteView(BaseDeleteView):
    """View to handle BiopsyOrder delete."""

    model = BiopsyRequest
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia eliminada satisfactoriamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"


class BiopsyRequestAddDiagnosticView(BaseCreateView):
    """View to handle BiopsyOrder view."""

    model = Head
    form_class = HeadBiopsyForm
    success_url = reverse_lazy("pathologic_anathomy:biopsy-verificated_list")
    success_message = "Diagnostico de biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    
    def form_valid(self, form):
        if form.is_valid():
            biopsy = form.cleaned_data["biopsy"]
            biopsy.verificated = True
            biopsy.save()
            return super().form_valid(form)
