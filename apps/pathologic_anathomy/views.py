from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from apps.core.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseUpdateView,
)
from apps.pathologic_anathomy.forms import BiopsyRequestForm
from apps.pathologic_anathomy.forms_biopsy_diagnostic import (
    form_head,
    form_neck,
    form_stomac,
    form_linfoma,
    form_gynecology,
    form_mama_cdi,
    form_mama_cdis,
)
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic import (
    model_head,
    model_neck,
    model_stomac,
    model_linfoma,
    model_gynecology,
    model_mama_cdi,
    model_mama_cdis,
)


# Create your views here.
class BiopsyRequestCreateView(BaseCreateView):
    """View to handle BiopsyOrder view."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"


class BiopsyRequestDetailView(BaseDetailView):
    """View to handle BiopsyOrder details."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Orden de biopsia no encontrada"


class BiopsyRequestUpdateView(BaseUpdateView):
    """View to handle BiopsyOrder edition."""

    model = BiopsyRequest
    form_class = BiopsyRequestForm
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia guardada correctamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"


class BiopsyRequestDeleteView(BaseDeleteView):
    """View to handle BiopsyOrder delete."""

    model = BiopsyRequest
    success_url = reverse_lazy("pathologic_anathomy:biopsyrequest_list")
    success_message = "Biopsia eliminada satisfactoriamente."
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    object_not_found_error_message = "Biopsia no encontrada"

class BiopsyDiagnosticatedDeleteView(BaseDeleteView):
    """View to handle Biopsys diagnosticated delete."""

    model = BiopsyRequest
    success_url = reverse_lazy("pathologic_anathomy:biopsy-diagnosticated_list")
    success_message = "Biopsia eliminada satisfactoriamente."
    cancel_url = "pathologic_anathomy:biopsy-diagnosticated_list"
    object_not_found_error_message = "Biopsia no encontrada"    

#ADD DIAGNOSTIC
BIOPSY_TYPES = {
        1:{"model":model_head.Head, "form":form_head.HeadBiopsyForm},  #Cabeza
        2:{"model":model_neck.NeckBiopsyDiagnostic, "form":form_neck.NeckBiopsyDiagnosticForm},  #Biopsia de Cuello
        3:{"model":model_stomac.StomacBiopsyDiagnostic, "form":form_stomac.StomacBiopsyDiagnosticForm},  #Biopsia Digestivo
        4:{"model":model_gynecology.GynecologyBiopsyDiagnostic, "form":form_gynecology.GynecologyBiopsyForm},  #Biopsia de Ginecologia
        5:{"model":model_linfoma.LinfomaBiopsyDiagnostic, "form":form_linfoma.LinfomaBiopsyDiagnosticForm},  #Biopsia de Linfoma
        6:{"model":model_mama_cdi.MamaCDIBiopsyDiagnostic, "form":form_mama_cdi.MamaCDIBiopsyForm},  #Biopsia de Mama CDI
        7:{"model":model_mama_cdis.MamaCDISBiopsyDiagnostic, "form":form_mama_cdis.MamaCDISBiopsyForm},  #Biopsia de Mama CDIS
    }    

def get_form_class(biopsy):
    '''Return the form class corresponding to the current biopsy'''
    return BIOPSY_TYPES[biopsy.biopsy_type]["form"] 

def get_model_class(biopsy):
    '''Return the model class corresponding to the form of the biopsy'''
    return BIOPSY_TYPES[biopsy.biopsy_type]["model"] 

def disable_form_fields(form):
    for field in form.fields.values():
        field.disabled = True
    
def add_diagnostic_view(request, biopsy_pk):
    success_url = reverse_lazy("pathologic_anathomy:biopsy-diagnosticated_list")
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    biopsy = BiopsyRequest.objects.get(pk = biopsy_pk)
    view_title = f"Añadir {get_model_class(biopsy)._meta.verbose_name.lower()} de la biopsia {biopsy.biopsy_id}"
    #si es post procesamos el formulario para guardarlo o mostrar los errores
    if request.method == "POST":
        form = get_form_class(biopsy)(request.POST)
        if form.is_valid():
            biopsy.verificated = True
            biopsy.save()
            form.save()
            return redirect(success_url) 
        else:
            # Renderiza el formulario con los errores
            return render(
                request, 
                "pathologic_anathomy/add_diagnostic.html", 
                {
                    "form": form, 
                    "cancel_url":"pathologic_anathomy:biopsyrequest_list",
                    "view_title":view_title,
                }
                )                    
    #mostramos el formulario en el template
    else:
        form = get_form_class(biopsy)(initial={'biopsy': biopsy_pk})
        form_biopsyrequest = BiopsyRequestForm(instance = biopsy)
        disable_form_fields(form_biopsyrequest)
        return render(
            request, 
            "pathologic_anathomy/add_diagnostic.html", 
            {
                "form": form, 
                "form_biopsyrequest": form_biopsyrequest,
                "cancel_url":cancel_url,
                "view_title":view_title,
             }
            )

def biopsy_diagnosticated_detail_view(request, biopsy_pk):
    biopsy = BiopsyRequest.objects.get(pk = biopsy_pk)
    diagnostic = get_model_class(biopsy).objects.get(biopsy = biopsy_pk)
    view_title = f"Detalles del {get_model_class(biopsy)._meta.verbose_name.lower()} {biopsy.biopsy_id}"
    
    print(diagnostic)
    form = get_form_class(biopsy)(instance = diagnostic)
    form_biopsyrequest = BiopsyRequestForm(instance = biopsy)
    disable_form_fields(form_biopsyrequest)
    disable_form_fields(form)
    return render(
        request, 
        "pathologic_anathomy/biopsy_diagnosticated_detail.html", 
        {
            "form": form, 
            "form_biopsyrequest": form_biopsyrequest,
            "view_title":view_title,
            }
        )        

def biopsy_diagnostic_update_view(request, biopsy_pk):
    success_url = reverse_lazy("pathologic_anathomy:biopsy-diagnosticated_list")
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    biopsy = BiopsyRequest.objects.get(pk = biopsy_pk)
    diagnostic = get_model_class(biopsy).objects.get(biopsy = biopsy_pk)
    view_title = f"Añadir {get_model_class(biopsy)._meta.verbose_name.lower()} de la biopsia {biopsy.biopsy_id}"
    #si es post procesamos el formulario para guardarlo o mostrar los errores
    if request.method == "POST":
        form = get_form_class(biopsy)(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(success_url) 
        else:
            # Renderiza el formulario con los errores
            return render(
                request, 
                "pathologic_anathomy/add_diagnostic.html", 
                {
                    "form": form, 
                    "cancel_url":"pathologic_anathomy:biopsyrequest_list",
                    "view_title":view_title,
                }
                )                    
    #mostramos el formulario en el template
    else:
        form = get_form_class(biopsy)(instance = diagnostic)
        form_biopsyrequest = BiopsyRequestForm(instance = biopsy)
        disable_form_fields(form_biopsyrequest)
        return render(
            request, 
            "pathologic_anathomy/biopsy_diagnostic_update.html", 
            {
                "form": form, 
                "form_biopsyrequest": form_biopsyrequest,
                "cancel_url":cancel_url,
                "view_title":view_title,
             }
            )        