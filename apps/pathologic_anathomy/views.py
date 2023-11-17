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
)
from apps.pathologic_anathomy.models import BiopsyRequest
from apps.pathologic_anathomy.models_biopsy_diagnostic import (
    model_head,
    model_neck,
    model_stomac,
    model_linfoma,
    model_gynecology,
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

#ADD DIAGNOSTIC
BIOPSY_TYPES = {
        1:{"model":model_head.Head, "form":form_head.HeadBiopsyForm},  #Biopsia de Mama
        2:{"model":model_neck.NeckBiopsyDiagnostic, "form":form_neck.NeckBiopsyDiagnosticForm},  #Biopsia de Cuello
        3:{"model":model_stomac.StomacBiopsyDiagnostic, "form":form_stomac.StomacBiopsyDiagnosticForm},  #Biopsia Digestivo
        4:{"model":model_linfoma.LinfomaBiopsyDiagnostic, "form":form_linfoma.LinfomaBiopsyDiagnosticForm},  #Biopsia de Linfoma
        5:{"model":model_gynecology.GynecologyBiopsyDiagnostic, "form":form_gynecology.GynecologyBiopsyForm},  #Biopsia de Ginecologia
        6:{"model":model_head.Head, "form":form_head.HeadBiopsyForm},  #Biopsia de Cabeza
    }    

def get_form_class(biopsy):
    '''Return the form class corresponding to the current biopsy'''
    return BIOPSY_TYPES[biopsy.biopsy_type]["form"] 

def get_model_class(biopsy):
    '''Return the model class corresponding to the form of the biopsy'''
    return BIOPSY_TYPES[biopsy.biopsy_type]["model"] 
    
def add_diagnostic_view(request, biopsy_pk):
    success_url = reverse_lazy("pathologic_anathomy:biopsy-diagnosticated_list")
    cancel_url = "pathologic_anathomy:biopsyrequest_list"
    biopsy = BiopsyRequest.objects.get(pk = biopsy_pk)
    view_title = f"Añadir {get_model_class(biopsy)._meta.verbose_name.lower()} de la biopsia {biopsy.biopsy_id}"
    #si es post procesamos el formulario para guardarlo o mostrar los errores
    if request.method == "POST":
        form = get_form_class(biopsy)(request.POST)
        print(form)
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
        form = form_head.HeadBiopsyForm(initial={'biopsy': biopsy_pk})
        return render(
            request, 
            "pathologic_anathomy/add_diagnostic.html", 
            {
                "form": form, 
                "cancel_url":cancel_url,
                "view_title":view_title,
             }
            )

        