# Create your views here.
from django.shortcuts import render


def asdf(request):
    return render(request, "base_crud/base_crud.html", context={"crud_name": "TEST"})
