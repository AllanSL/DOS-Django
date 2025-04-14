from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("listarusuarios/", views.listarUsuarios, name="listarusuarios"),
    path("listartarefas/", views.listarTarefas, name="listartarefas"),
    path("cadastrartarefas", views.cadastrarTarefas, name="cadastrartarefas"),
    path("cadastrarusuarios", views.cadastrarUsuarios, name="cadastrarusuarios"),
    path('logout/', views.logout_view, name='logout'),
    path("login/", views.login_view, name="login"),

    
    path("editarusuario/<int:id>/", views.editarUsuario, name="editarusuario"),
    path("excluirusuario/<int:id>/", views.excluirUsuario, name="excluirusuario"),
    
    path("editartarefa/<int:id>/", views.editarTarefa, name="editartarefa"),
    path("excluirtarefa/<int:id>/", views.excluirTarefa, name="excluirtarefa"),

]