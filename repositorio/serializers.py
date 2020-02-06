from rest_framework import serializers
from repositorio.models import *
from django.core.mail import EmailMessage
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

class ContactoSerializer(serializers.Serializer):
    nombres = serializers.CharField()
    correo = serializers.CharField()
    tema = serializers.CharField()
    mensaje = serializers.CharField()
    def create(self, validated_data):
        instance=Contacto()
        instance.nombres=validated_data.get("nombres")
        instance.correo=validated_data.get("correo")
        instance.tema=validated_data.get("tema")
        instance.mensaje=validated_data.get("mensaje")
        email= EmailMessage(
            validated_data.get("tema"),
            validated_data.get("mensaje"),
            'fksaxell1997@gmail.com',
            ['wipitik239@xmailsme.com']
        )
        email.send()
        instance.save()
        return instance
    def validate_correo(self,data):
        correos = Contacto.objects.filter(correo=data)
        if len(correos)!=0:
            raise serializers.ValidationError('Este correo ya ha enviado un msj')
        else:
            data


