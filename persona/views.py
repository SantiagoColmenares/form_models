from django.shortcuts import render
from .form import PersonaForm, DocumentoForm
from .models import Persona, Documento
# Create your views here.

def create_persona(request):
    documento = request.POST.get('documento_identidad')
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonaForm()
    return render(request, 'persona.html', {'form': form, 'documento': documento})

def create_document(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DocumentoForm()
    return render(request, 'documento.html', {'form':form})
    


