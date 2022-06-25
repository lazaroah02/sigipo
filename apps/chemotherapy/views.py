from typing import Any

from django.forms import CheckboxInput, inlineformset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from apps.chemotherapy.forms import (
    CycleForm,
    CycleMedicationForm,
    MedicationForm,
    ProtocolForm,
    SchemeForm,
)
from apps.chemotherapy.models import (
    Cycle,
    CycleMedication,
    Medication,
    Protocol,
    Scheme,
)
from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)


# * Scheme Views
class SchemeCreateView(BaseCreateView):
    """View to handle Scheme creation."""

    model = Scheme
    form_class = SchemeForm
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "chemotherapy:scheme_list"
    permission_required = "chemotherapy_manage"


class SchemeDetailView(BaseDetailView):
    """View to handle Scheme details."""

    model = Scheme
    form_class = SchemeForm
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_view"


class SchemeUpdateView(BaseUpdateView):
    """View to handle Scheme edition."""

    model = Scheme
    form_class = SchemeForm
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s guardado correctamente."
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_manage"


class SchemeDeleteView(BaseDeleteView):
    """View to handle Scheme delete."""

    model = Scheme
    success_url = reverse_lazy("chemotherapy:scheme_list")
    success_message = "%(name)s eliminado satisfactoriamente."
    cancel_url = "chemotherapy:scheme_list"
    object_not_found_error_message = "Esquema no encontrado"
    permission_required = "chemotherapy_manage"


# * Protocol Views
class ProtocolCreateView(BaseCreateView):
    """View to handle Protocol creation."""

    model = Protocol
    form_class = ProtocolForm
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "chemotherapy:protocol_list"
    permission_required = "chemotherapy_manage"


class ProtocolDetailView(BaseDetailView):
    """View to handle Protocol details."""

    model = Protocol
    form_class = ProtocolForm
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_view"


class ProtocolUpdateView(BaseUpdateView):
    """View to handle Protocol edition."""

    model = Protocol
    form_class = ProtocolForm
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s guardado correctamente."
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_manage"


class ProtocolDeleteView(BaseDeleteView):
    """View to handle Protocol delete."""

    model = Protocol
    success_url = reverse_lazy("chemotherapy:protocol_list")
    success_message = "%(patient)s eliminado satisfactoriamente."
    cancel_url = "chemotherapy:protocol_list"
    object_not_found_error_message = "Protocolo no encontrado"
    permission_required = "chemotherapy_manage"


# * Medication Views


class MedicationCreateView(BaseCreateView):
    """View to handle Medication creation."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    permission_required = "chemotherapy_manage"


class MedicationDetailView(BaseUpdateView):
    """View to handle Medication details."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_view"


class MedicationUpdateView(BaseUpdateView):
    """View to handle Medication edition."""

    model = Medication
    form_class = MedicationForm
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación guardada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_manage"


class MedicationDeleteView(BaseDeleteView):
    """View to handle Medication delete."""

    model = Medication
    success_url = reverse_lazy("chemotherapy:medication_list")
    success_message = "Medicación eliminada correctamente."
    cancel_url = "chemotherapy:medication_list"
    object_not_found_error_message = "Medicación no encontrada"
    permission_required = "chemotherapy_manage"


# * Cycle Views


class CycleCreateView(BaseCreateView):
    """View to handle Cycle creation."""

    model = Cycle
    form_class = CycleForm
    success_url = reverse_lazy("chemotherapy:cycle_list")
    success_message = "Ciclo guardado correctamente."
    cancel_url = "chemotherapy:cycle_list"
    template_name = "chemotherapy/cycle_update.html"
    permission_required = "chemotherapy_manage"
    Cycle_Cycle_Medication = inlineformset_factory(
        Cycle,
        CycleMedication,
        form=CycleMedicationForm,
        fk_name="cycle",
        extra=1,
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = self.Cycle_Cycle_Medication()
        for form in context["formset"]:
            form.fields["DELETE"].widget.attrs["class"] = "form-check-input"
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = self.Cycle_Cycle_Medication(
            self.request.POST,
        )
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save(commit=False)
        self.object.save()

        formset = formset.save(commit=False)
        for cycle_medication in formset:
            cycle_medication.cycle = self.object
            cycle_medication.save()
        return redirect(self.success_url)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class CycleDetailView(BaseDetailView):
    """View to handle Cycle detail."""

    model = Cycle
    form_class = CycleForm
    cancel_url = "chemotherapy:cycle_list"
    template_name = "chemotherapy/cycle_detail.html"
    permission_required = "chemotherapy_manage"
    Cycle_Cycle_Medication = inlineformset_factory(
        Cycle,
        CycleMedication,
        form=CycleMedicationForm,
        fk_name="cycle",
        extra=0,
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cycle = self.get_object()
        context["formset"] = self.Cycle_Cycle_Medication(
            instance=cycle,
            queryset=CycleMedication.objects.filter(cycle=cycle),
        )
        for form in context["formset"]:
            form.fields["DELETE"].widget.attrs["class"] = "form-check-input"
            for _, field in form.fields.items():
                field.widget.attrs["readonly"] = True
                if isinstance(field.widget, CheckboxInput):
                    field.widget.attrs["disabled"] = True
        return context


class CycleUpdateView(BaseUpdateView):
    """View to handle Cycle update."""

    model = Cycle
    form_class = CycleForm
    success_url = reverse_lazy("chemotherapy:cycle_list")
    success_message = "Ciclo guardado correctamente."
    cancel_url = "chemotherapy:cycle_list"
    template_name = "chemotherapy/cycle_update.html"
    permission_required = "chemotherapy_manage"
    Cycle_Cycle_Medication = inlineformset_factory(
        Cycle,
        CycleMedication,
        form=CycleMedicationForm,
        fk_name="cycle",
        extra=1,
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cycle = self.get_object()
        context["formset"] = self.Cycle_Cycle_Medication(
            instance=cycle,
            queryset=CycleMedication.objects.filter(cycle=cycle),
        )
        for form in context["formset"]:
            form.fields["DELETE"].widget.attrs["class"] = "form-check-input"
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        cycle = self.get_object()
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = self.Cycle_Cycle_Medication(
            self.request.POST,
            instance=cycle,
            queryset=CycleMedication.objects.filter(cycle=cycle.pk),
        )
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save(commit=False)
        self.object.save()

        formset = formset.save(commit=False)
        for cycle_medication in formset:
            cycle_medication.cycle = self.object
            cycle_medication.save()
        return redirect(self.success_url)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class CycleDeleteView(BaseDeleteView):
    """View to handle Cycle detail."""

    model = Cycle
    cancel_url = "chemotherapy:cycle_list"
    success_url = reverse_lazy("chemotherapy:cycle_list")
    object_not_found_error_message = "Ciclo no encontrado"
    success_message = "Ciclo eliminado correctamente."
    permission_required = "chemotherapy_manage"
