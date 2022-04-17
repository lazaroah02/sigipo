from django.contrib.admin import register

from apps.classifiers.models import Morphology, Topography

register((Morphology, Topography))
