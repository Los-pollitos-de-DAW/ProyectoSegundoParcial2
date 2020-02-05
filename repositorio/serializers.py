from rest_framework import serializers
from repositorio.models import *
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields=('id','nombreRol')
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('id','rol','nombreCliente','usuario','password','estado','correo')

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noticia
        fields=('id','usuario','nombreNoticia','descrNoticia','creadoFecha')

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields=('id','nombreCarrera','codigo','img')

class TerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Termino
        fields=('id','nombreTermino')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields=('id','carrera','nombreMateria','tag')

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro
        fields=('id','termino','usuario','materia')

class DescargaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Descarga
        fields=('idD','idRegistro','fecha')

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Examen
        fields=('id','materia','titulo','termino','url')

