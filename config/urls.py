"""sigipo URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.accounts.views import asdf

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("apps.accounts.urls")),
    path("test/", asdf),
    path("geographic_location/", include("apps.geographic_location.urls")),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
