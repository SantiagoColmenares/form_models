from django.db import models

# Create your models here.
class Documento(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField(max_length=250)
    tipo_documento = models.ForeignKey(Documento, on_delete=models.PROTECT, null= False)
    fecha_nacimiento = models.DateField()