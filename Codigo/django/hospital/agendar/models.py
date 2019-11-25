from django.db import models
from login.models import Usuario

class DateReserva(models.Model):
	Id = models.AutoField(primary_key=True)
	Rut = models.CharField(max_length=30)
	Fecha_Visita = models.DateField()
	Latitud = models.CharField(max_length=30)
	Longitud = models.CharField(max_length=30)


	def __str__(self):
		return "{}".format(self.Rut)



