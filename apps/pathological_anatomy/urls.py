from django.urls import path

from apps.core.views import PaginationFilterView, getUrl

from apps.pathological_anatomy.filters import (
    PathologyFilter
)


from apps.pathological_anatomy.models import (
    Pathology
)

from apps.pathological_anatomy.views import (
    PathologyCreateView,
    PathologyDetailView,
    PathologyUpdateView,
    PathologyDeleteView,
)

app_name = "pathological_anatomy"
urlpatterns = [
    # * Pathology URLs
    path(
        "pathology/list/",
        PaginationFilterView.as_view(
            model=Pathology,
            filterset_class=PathologyFilter,
            permission_required="accounts.pathological_anatomy_view",
        ),
        name="pathology_list",
    ),
    getUrl(PathologyCreateView),
    getUrl(PathologyDetailView),
    getUrl(PathologyUpdateView),
    getUrl(PathologyDeleteView),
]