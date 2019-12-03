from django.db import models
from login.models import Especialista, Datos_Personales

class Crear(models.Model):
	Id = models.AutoField(primary_key = True)
	Nombre = models.CharField(max_length=10, default='')
	def __str__(self):
		return self.Nombre

class Registrar(models.Model):
    Id= models.ForeignKey(Crear, null=False, blank= True, on_delete =models.CASCADE)	
    Rut = models.ForeignKey(Especialista, null=False, blank=True, on_delete=models.CASCADE)
    def __str__(self):
    	return self.Id
