from django.db import models


class Datos_Personales(models.Model):
	idDatosPer = models.IntegerField(primary_key=True)
	Primer_Nombre = models.CharField(max_length=30)
	Segundo_Nombre = models.CharField(max_length=30)
	Primer_Apellido = models.CharField(max_length=30)
	Segundo_Apellido = models.CharField(max_length=30)
	Domicilio = models.CharField(max_length=30)
	Comuna = models.CharField(max_length=30)
	Telefono = models.CharField(max_length=30)
	Rut = models.CharField(max_length=30)
	Nacionalidad = models.CharField(max_length=30)
	Fecha_Nacimiento = models.DateField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)


class Usuario(Datos_Personales):
	Cargo = models.IntegerField()
	Email = models.CharField(max_length=30)


def __unicode__(self):
	return self.Email

def __str__(self):
	return self.Email

def get_absolute_url(self):
	return reverse("detail", kwargs={"id",self.idDatosPer})