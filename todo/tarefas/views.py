from django.shortcuts import render
from .models import Tarefas

def listarTarefas(request):
    tarefas = Tarefas.objects.all()
    return render(request, "listarTarefas.html", {"tarefas": tarefas})
