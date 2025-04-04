from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import Tarefa, Usuario

def index(request):
    return render(request, 'index.html')

def listarTarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "listarTarefas.html", {"tarefas": tarefas}) 


def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "listarUsuarios.html", {"usuarios": usuarios})

def cadastrarTarefas(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_str = request.POST.get('data')  # Captura apenas a data (YYYY-MM-DD)
        hora_str = request.POST.get('hora')  # Captura apenas a hora (HH:MM)

        # Junta data e hora no formato correto antes de converter
        data_completa_str = f"{data_str} {hora_str}"
        data = datetime.strptime(data_completa_str, "%Y-%m-%d %H:%M")  # Converte para datetime

        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, data=data, usuario=usuario)
        nova_tarefa.save()

    usuarios = Usuario.objects.all()
    return render(request, "cadastrarTarefas.html", {"usuarios": usuarios})

def cadastrarUsuarios(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.save()

        return redirect('/tarefas/listarusuarios')  # Redireciona para a lista de usuários após cadastro

    return render(request, "cadastrarUsuarios.html")

# Editar Usuário
def editarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    if request.method == "POST":
        usuario.nome = request.POST.get("nome")
        usuario.email = request.POST.get("email")
        usuario.save()
        return redirect("/tarefas/listarusuarios")
    
    return render(request, "editarUsuario.html", {"usuario": usuario})

# Excluir Usuário
def excluirUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect("/tarefas/listarusuarios")

# Editar Tarefa
def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    
    if request.method == "POST":
        tarefa.titulo = request.POST.get("titulo")
        tarefa.descricao = request.POST.get("descricao")
        tarefa.data = datetime.strptime(request.POST.get("data"), "%Y-%m-%dT%H:%M")
        tarefa.usuario_id = request.POST.get("usuario")
        tarefa.save()
        return redirect("/tarefas/listartarefas")
    
    usuarios = Usuario.objects.all()
    return render(request, "editarTarefa.html", {"tarefa": tarefa, "usuarios": usuarios})

# Excluir Tarefa
def excluirTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("/tarefas/listartarefas")