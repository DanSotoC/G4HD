from django.db import models

class Visita(models.Model):
	fecha = models.DateField(null=False)
	id_paciente = models.IntegerField(null=False)
