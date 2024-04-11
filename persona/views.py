from django.shortcuts import render
from .form import PersonaForm
from .models import Persona, Documento
# Create your views here.

def create_persona(request):
    form = PersonaForm(request.POST)
    return render(request, 'persona.html', {'form':form})
    


