from django.contrib import admin
from .models import Tarefas
from .models import Usuario

# Register your models here.

admin.site.register(Tarefas)
admin.site.register(Usuario)