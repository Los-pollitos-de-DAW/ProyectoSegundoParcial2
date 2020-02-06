from django.db import models
from django.utils import timezone
# Create your models here.
class Rol(models.Model):
    nombreRol=models.CharField(max_length=200)

class Usuario(models.Model):
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    nombreCliente= models.CharField(max_length=500)
    usuario=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    estado=models.BooleanField()
    correo=models.CharField(max_length=500)
class Noticia(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombreNoticia=models.CharField(max_length=500)
    descrNoticia=models.CharField(max_length=500)
    creadoFecha = models.DateTimeField(default=timezone.now)

class Carrera(models.Model):
    nombreCarrera=models.CharField(max_length=500)
    codigo=models.CharField(max_length=200)
    img=models.CharField(max_length=500)


class Termino(models.Model):
    nombreTermino=models.CharField(max_length=500)

class Materia(models.Model):
    carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    nombreMateria=models.CharField(max_length=500)
    tag=models.CharField(max_length=200)


class Registro(models.Model):
    termino=models.ForeignKey(Termino,on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE)

class Descarga(models.Model):
    idRegistro = models.ForeignKey(Registro,on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

class Examen(models.Model):
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=500)
    termino=models.CharField(max_length=500)
    url=models.CharField(max_length=500)

class Contacto(models.Model):
    nombres=models.CharField(max_length=500)
    correo=models.CharField(max_length=500)
    tema=models.CharField(max_length=500)
    mensaje=models.CharField(max_length=800)

