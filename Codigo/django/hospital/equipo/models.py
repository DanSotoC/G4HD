from django.db import models
from login.models import Especialista, Datos_Personales

class Equipo(models.Model):
	id_equipo = models.AutoField(primary_key = True)
	nombre_equipo = models.CharField(max_length=1, default='A')
	funcionario = models.ForeignKey(Especialista, null=True, blank=True, on_delete=models.CASCADE	)


