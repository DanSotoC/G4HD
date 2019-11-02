from django.db import models
from login.models import Especialista, Datos_Personales

class Equipo(models.Model):
	id_equipo = models.IntegerField(primary_key = True)
	cant_funcionarios = models.IntegerField()
	
	
class Asignar(Equipo):
	funcionario = models.ForeignKey(Especialista, null=False, blank=True, on_delete=models.CASCADE)
