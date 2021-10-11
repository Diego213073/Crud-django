from django.shortcuts import redirect, render
from .models import Persona
from .formulario import formularioPersona

# Create your views here.


def listarPersonas(request):

    personas = Persona.objects.all()
    diccionario_lista_personas = {
        'personas':personas
    }
    return render(request,'index.html',diccionario_lista_personas)


def crearPersona(request):
    ctx = None
    if request.method == "GET":
      formulario = formularioPersona()
      ctx = {'formulario':formulario}
    else:
      formulario = formularioPersona(request.POST)
      ctx = {'formulario':formulario}
      if formulario.is_valid():
          formulario.save()
          return redirect('index')
    return render(request,'crear.html',ctx)


def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == "GET":
        formulario = formularioPersona(instance=persona)
        ctx = {"formulario":formulario}
    else:
        formulario = formularioPersona(request.POST,instance=persona)
        ctx = {"formulario":formulario}
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request,'crear.html', ctx)


def eliminar(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')
