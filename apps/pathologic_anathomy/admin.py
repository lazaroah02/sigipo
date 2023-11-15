# Register your models here.
from django.contrib import admin

from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic import (
    model_head,
    model_linfoma,
    model_neck,
    model_stomac,
)

admin.site.register(BiopsyRequest)
admin.site.register(model_head.Head)
admin.site.register(model_neck.NeckBiopsyDiagnostic)
admin.site.register(model_stomac.StomacBiopsyDiagnostic)
admin.site.register(model_linfoma.LinfomaBiopsyDiagnostic)
