from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import CheckboxInput
from django.http import Http404, HttpRequest
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
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
        self.extra_context = self.extra_context or {}
        context["parameters"] = parameters
        context["url_lookup"] = self.request.GET.urlencode()
        current_page = context["page_obj"].number
        paginator = context["paginator"]
        pagination_range = paginator.get_elided_page_range(
            current_page, on_each_side=2, on_ends=0
        )
        if self.model is not None:
            CURRENT_MODEL = self.model
            MODEL_NAME = self.model.__name__.lower()
        else:
            CURRENT_MODEL = self.queryset.model
            MODEL_NAME = self.queryset.model.__name__.lower()
        pagination_range = list(
            filter(lambda element: element != paginator.ELLIPSIS, pagination_range)
        )
        context["pagination_range"] = pagination_range
        APP_NAME = (
            context.get("app_name", None) or CURRENT_MODEL._meta.app_label.lower()
        )
        context["crud_name"] = (
            CURRENT_MODEL._meta.verbose_name_plural.capitalize() or context["crud_name"]
        )
        context["crud_instance_name"] = (
            CURRENT_MODEL._meta.verbose_name.lower() or context["crud_instance_name"]
        )
        context["add_url"] = f"{APP_NAME}:{MODEL_NAME}_create" or context["add_url"]
        context["detail_url"] = (
            f"{APP_NAME}:{MODEL_NAME}_detail" or context["detail_url"]
        )
        context["edit_url"] = f"{APP_NAME}:{MODEL_NAME}_update" or context["edit_url"]
        context["delete_url"] = (
            f"{APP_NAME}:{MODEL_NAME}_delete" or context["delete_url"]
        )

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


def getUrl(crud_class):
    if issubclass(crud_class, BaseCreateView):
        model_name = crud_class.model.__name__.lower()
        return path(
            f"{model_name}/create/",
            crud_class.as_view(),
            name=f"{model_name}_create",
        )
    elif issubclass(crud_class, BaseUpdateView):
        model_name = crud_class.model.__name__.lower()
        return path(
            f"{model_name}/update/<pk>/",
            crud_class.as_view(),
            name=f"{model_name}_update",
        )
    elif issubclass(crud_class, BaseDetailView):
        model_name = crud_class.model.__name__.lower()
        return path(
            f"{model_name}/detail/<pk>/",
            crud_class.as_view(),
            name=f"{model_name}_detail",
        )
    else:
        model_name = crud_class.model.__name__.lower()
        return path(
            f"{model_name}/delete/<pk>/",
            crud_class.as_view(),
            name=f"{model_name}_delete",
        )
