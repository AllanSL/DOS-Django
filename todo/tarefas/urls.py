from .views import listarTarefas
from django.urls import path

urlpatterns = [
    path('listartarefas/', listarTarefas),
]