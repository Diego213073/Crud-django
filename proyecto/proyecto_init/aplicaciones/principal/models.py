from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField(max_length= 50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField
    correo = models.EmailField(max_length=1500)
