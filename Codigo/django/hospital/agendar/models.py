from django.db import models
from login.models import Usuario

class DateReserva(models.Model):
	Id = models.AutoField(primary_key=True)
	Rut = models.ForeignKey(Usuario, null=False, blank= True, on_delete =models.CASCADE)	
	Fecha_Visita = models.DateField()

