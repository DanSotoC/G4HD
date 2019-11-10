from django.db import models
from django.urls import reverse


class Datos_Personales(models.Model):
	idDatosPer = models.AutoField(primary_key=True)
	Primer_Nombre = models.CharField(max_length=30)
	Primer_Apellido = models.CharField(max_length=30)
	Segundo_Apellido = models.CharField(max_length=30)
	Telefono = models.CharField(max_length=30)
	Rut = models.CharField(max_length=30)
	Nacionalidad = models.CharField(max_length=30)
	Fecha_Nacimiento = models.DateField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
	
	def __str__(self):
		return self.Rut


class Usuario(Datos_Personales):
	Cargo = models.IntegerField(default=1)
	Email = models.CharField(max_length=30)
	Nombre_Completo_Tutor = models.CharField(max_length=60,default='')
	Rut_Tutor = models.CharField(max_length=30,default='')
	Domicilio = models.CharField(max_length=50, default='')
	Comuna = models.CharField(max_length=30, default='')

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id":self.idDatosPer})


class Especialista(Datos_Personales):
	Cargo = models.IntegerField(default=2)
	Email = models.CharField(max_length=30,default='')

	def get_absolute_url(self):
		return reverse("detailes", kwargs={"id":self.idDatosPer})