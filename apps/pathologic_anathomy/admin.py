# Register your models here.
from django.contrib import admin
from .models import BiopsyRequest
from .models_biopsy_diagnostic import model_head
 
admin.site.register(BiopsyRequest)
admin.site.register(model_head.Head)
