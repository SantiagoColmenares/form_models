from django.urls import path
from . import views

urlpatterns = [
    path('Persona/', views.create_persona, name="create_persona"),
    path('Documento/', views.create_document, name="create_document")
]
