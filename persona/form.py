from django import forms 
from .models import Persona, Documento


class DocumentoForm(forms.ModelForm):
     class Meta:
         model = Documento
         fields = ['tipo']
         widgets = {
             'tipo': forms.TextInput(attrs={'type':'text'})
         }


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'correo', 'tipo_documento', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),

            'apellido': forms.TextInput(attrs={'type':'text',
                                             'class':'form__control'}),

            'correo': forms.EmailInput(attrs={'type':'email',
                                             'class':'form__control'}),

            'tipo_documento': forms.Select(attrs={'class':'form__control'}),

            'fecha_nacimiento': forms.DateInput(attrs={'type':'date',
                                                'class':'form__control'}),
        }


        
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Persona.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return correo

        
