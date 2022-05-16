from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import CheckboxInput
from django.http import Http404, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView


class PaginationFilterView(LoginRequiredMixin, FilterView):
    """FilterView with pagination."""

    paginate_by = 30
    extra_context: dict = None

    def get_ordering(self):
        """Return the field or fields to use for ordering the queryset."""
        ordering = self.request.GET.getlist(key="o", default=None)
        return ordering if len(ordering) > 0 else None

    def get_context_data(self, *args, **kwargs) -> dict:
        """
        Save the url lookup filters to use it in the url links.
        <a href="?page={{ page_obj.next_page_number }}&{{ parameters }}">
            Next
        </a>
        """
        _request_copy = self.request.GET.copy()
        parameters = _request_copy.pop("page", True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context["parameters"] = parameters
        context["url_lookup"] = self.request.GET.urlencode()
        current_page = context["page_obj"].number
        paginator = context["paginator"]
        pagination_range = paginator.get_elided_page_range(
            current_page, on_each_side=2, on_ends=0
        )
        pagination_range = list(
            filter(lambda element: element != paginator.ELLIPSIS, pagination_range)
        )
        context["pagination_range"] = pagination_range
        context |= self.extra_context
        return context


class CancelUrlMixin:
    """Mixin to add cancel url to django generics views."""

    cancel_url = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """Adds given url to the context."""
        context = super().get_context_data(*args, **kwargs)
        if not self.request.GET.get("return_to", False):
            context["cancel_url"] = self.cancel_url
        else:
            _request_copy = self.request.GET.copy()
            parameters = (
                _request_copy.pop("return_to", True) and _request_copy.urlencode()
            )
            context["cancel_url"] = self.request.GET.get("return_to")
            context["url_lookup"] = parameters
        return context

    def get_cancel_url(self):
        """Returns cancel url."""
        return reverse_lazy(self.cancel_url)


class ViewTitleMixin:
    """Mixin to view title to django generics views."""

    title = None

    def get_context_data(self, *args, **kwargs) -> dict:
        """Adds given title to the context."""
        context = super().get_context_data(*args, **kwargs)
        context["view_title"] = self.title
        return context


class GetObjectErrorMixin:
    """Generate user friendly message for object not found exception."""

    object_not_found_error_message = None

    def get(self, request: HttpRequest, *args, **kwargs):
        """Override get_object to handle object not found exception."""
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, self.object_not_found_error_message)
            return redirect(self.get_cancel_url())
        return super().get(request, *args, **kwargs)


class BaseCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CancelUrlMixin, ViewTitleMixin, CreateView
):
    """Base create view."""

    template_name = "base_crud/base_create.html"

    def __init__(self, **kwargs):
        self.title = f"Añadir {self.model._meta.verbose_name.lower()}"
        super().__init__(**kwargs)


class BaseUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    GetObjectErrorMixin,
    CancelUrlMixin,
    ViewTitleMixin,
    UpdateView,
):
    """Base update view."""

    template_name = "base_crud/base_update.html"

    def __init__(self, **kwargs):
        self.title = f"Editar {self.model._meta.verbose_name.lower()}"
        super().__init__(**kwargs)


class BaseDetailView(
    LoginRequiredMixin,
    GetObjectErrorMixin,
    CancelUrlMixin,
    ViewTitleMixin,
    DetailView,
):
    """Base detail view."""

    template_name = "base_crud/base_detail.html"
    form_class = None

    def __init__(self, **kwargs):
        self.title = f"Detalles de {self.model._meta.verbose_name.lower()}"
        super().__init__(**kwargs)

    def get_form_for_detail(self):
        """Returns the form_class with all the fields in readonly."""

        class ReadOnlyForm(self.form_class):
            """Helper class"""

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for _, field in self.fields.items():
                    field.widget.attrs["readonly"] = True
                    if isinstance(field.widget, CheckboxInput):
                        field.widget.attrs["disabled"] = True

        return ReadOnlyForm

    def get_context_data(self, *args, **kwargs) -> dict:
        """Adds given form to the context."""
        context = super().get_context_data(*args, **kwargs)
        form = self.get_form_for_detail()(instance=self.object)

        context["form"] = form
        return context


class BaseDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    GetObjectErrorMixin,
    CancelUrlMixin,
    ViewTitleMixin,
    DeleteView,
):
    """Base delete view."""

    template_name = "base_crud/base_delete.html"

    def __init__(self, **kwargs):
        self.title = f"Eliminar {self.model._meta.verbose_name.lower()}"
        super().__init__(**kwargs)

    def delete(self, request: HttpRequest, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        success_message = self.get_success_message(self.object.__dict__)
        messages.success(self.request, success_message)
        return redirect(success_url)
