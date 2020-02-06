"""DawFin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from repositorio import views

router = routers.DefaultRouter()
router.register(r'noticia', views.NoticiaViewSet)
router.register(r'rol', views.RolViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'carrera', views.CarreraViewSet)
router.register(r'termino', views.TerminoViewSet)
router.register(r'materia', views.MateriaViewSet)
router.register(r'registro', views.RegistroViewSet)
router.register(r'descarga', views.DescargaViewSet)
router.register(r'examen', views.ExamenViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('email',views.ContactoAPI.as_view(),name="api_send_email"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
