from django.db import models

class Visita(models.Model):
	fecha = models.DateField(null=False)
	id_paciente = models.IntegerField(null=False)
	status = models.IntegerField(null=False, default=0) #0 = Activa 1= Completa 
