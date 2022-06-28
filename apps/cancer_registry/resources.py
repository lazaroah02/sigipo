from import_export.resources import ModelResource

from apps.cancer_registry.models import Neoplasm


class NeoplasmResource(ModelResource):
    class Meta:
        model = Neoplasm
