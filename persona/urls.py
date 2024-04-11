from django.urls import path
from . import views

urlpatterns = [
    path('Persona/', views.create_persona, name="cretae_persona")
]
