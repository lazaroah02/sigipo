"""sigipo URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
