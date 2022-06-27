import io

from django.db.models import Count
from django.http import FileResponse
from django.urls import reverse_lazy

from apps.cancer_registry.forms import NeoplasmForm
from apps.cancer_registry.models import Neoplasm
from apps.cancer_registry.report import (
    add_data_table,
    add_report_range,
    add_total,
    generate_report_header,
)
from apps.classifiers.models import Morphology
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
    ReportDownloadView,
)


# * Neoplasm Views
class NeoplasmCreateView(BaseCreateView):
    """View to handle neoplasm creation."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s guardada correctamente."
    cancel_url = "cancer_registry:neoplasm_list"
    title = "Añadir neoplasia"
    template_name = "cancer_registry/neoplasm_create.html"
    permission_required = "cancer_registry_manage"


class NeoplasmDetailView(BaseDetailView):
    """View to handle neoplasm details."""

    model = Neoplasm
    form_class = NeoplasmForm
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Detalles de neoplasia"
    template_name = "cancer_registry/neoplasm_detail.html"
    permission_required = "cancer_registry_view"


class NeoplasmUpdateView(BaseUpdateView):
    """View to handle neoplasm edition."""

    model = Neoplasm
    form_class = NeoplasmForm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s guardada correctamente."
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Editar neoplasia"
    template_name = "cancer_registry/neoplasm_update.html"
    permission_required = "cancer_registry_manage"


class NeoplasmDeleteView(BaseDeleteView):
    """View to handle neoplasm delete."""

    model = Neoplasm
    success_url = reverse_lazy("cancer_registry:neoplasm_list")
    success_message = "%(primary_site)s eliminada satisfactoriamente."
    cancel_url = "cancer_registry:neoplasm_list"
    object_not_found_error_message = "Neoplasia no encontrada"
    title = "Eliminar neoplasia"
    permission_required = "cancer_registry_manage"


class MorphologyReportView(ReportDownloadView):
    report_name = "Cantidad de casos por morfología"
    report_text = "Ingrese el intervalo de tiempo."

    def post(self, request, *args, **kwargs):
        form = self.report_form(request.POST)
        if form.is_valid():
            initial_date = form.cleaned_data["initial_date"]
            final_date = form.cleaned_data["final_date"]
            document = generate_report_header("CANTIDAD DE CASOS POR MORFOLOGÍA")
            add_report_range(document, initial_date, final_date)
            data = (
                Morphology.objects.annotate(test_count=Count("neoplasm"))
                .filter(test_count__gt=0)
                .only("name")
                .order_by("name")
            )
            add_data_table(
                document,
                data,
                columns=["Morfología", "Cantidad de casos"],
                queryset_columns=["name", "test_count"],
            )
            add_total(document, data, "test_count")
            buffer = io.BytesIO()
            document.save(buffer)
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="reporte.docx")
        else:
            return self.render_to_response(self.get_context_data(form=form))
