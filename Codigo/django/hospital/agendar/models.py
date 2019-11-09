from django.db import models
from login.models import Usuario

class DateReserva(models.Model):
	Id = models.AutoField(primary_key=True)
	Rut = models.CharField(max_length=30)
	Fecha_Visita = models.DateField()

	def __str__(self):
		return "{}".format(self.Rut)


