from django.forms import ModelForm
from .models import Persona, Documento


class DocumentoForm(ModelForm):
    class Meta:
        modelo = Documento
        fields = (__all__)
class PersonaForm(ModelForm):
    class Meta:
        modelo = Persona
        fields = (__all__)
        
