"""sigipo URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("", include("apps.dashboard.urls")),
    path("classifiers/", include("apps.classifiers.urls")),
    path("geographic_location/", include("apps.geographic_location.urls")),
    path("cancer_registry/", include("apps.cancer_registry.urls")),
    path("patient/", include("apps.patient.urls")),
    # * django-select2-urls
    path("select2/", include("django_select2.urls")),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
