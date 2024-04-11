from django import forms 
from .models import Persona, Documento


# class DocumentoForm(ModelForm):
#     class Meta:
#         modelo = Documento
#         fields = (__all__)
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'correo', 'tipo_documento', 'fecha_nac']
        widgets = {
            'nombre': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),

            'apellido': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),

            'correo': forms.EmailInput(attrs={'type':'email',
                                             'class':'form__control'}),

            'tipo_documento': forms.Select(attrs={'class':'form__control'}),

            'fecha_nac': forms.DateInput(attrs={'type':'date',
                                                'class':'form__control'}),
        }

        
