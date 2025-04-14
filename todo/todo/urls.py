from django.contrib import admin
from django.urls import path, include
from tarefas.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Página inicial vai pro login
    path('tarefas/', include(('tarefas.urls', 'tarefas'), namespace='tarefas')),  # <-- Adiciona o namespace
]
