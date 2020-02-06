from django.shortcuts import render
from django.utils import timezone
from .models import *
from rest_framework import generics
from repositorio.serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import EmailMessage

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class TerminoViewSet(viewsets.ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

class DescargaViewSet(viewsets.ModelViewSet):
    queryset = Descarga.objects.all()
    serializer_class =DescargaSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

def send_email():
    email = EmailMessage(
        'Title',
       'hola',
        'fksaxell1997@gmail.com',
        ['wipitik239@xmailsme.com']
    )

    email.send()
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class =ContactoSerializer
    def create(self, request, *args, **kwargs):
        response = super(ContactoViewSet, self).create(request, *args, **kwargs)
        send_email()  # sending mail
        return response




