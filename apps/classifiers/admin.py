from django.contrib.admin import site

from apps.classifiers.models import Morphology, Topography

site.register((Morphology, Topography))
