from django.shortcuts import render
from .models import Persona

# Create your views here.


def vistaInicio(resquest):

    return render(resquest,'index.html')
