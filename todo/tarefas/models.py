from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, default='')
    descricao = models.CharField(max_length=200, default='')
    data = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo