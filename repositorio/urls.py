from django.urls import path
from . import views

urlpatterns = [
    path('rol', views.RolList.as_view()),
    path('usuario',views.UsuarioList.as_view()),
    path('noticia',views.NoticiaList.as_view()),
]
