from django.db import models
<<<<<<< HEAD
from login.models import Especialista, Datos_Personales

class Equipo(models.Model):
	id_equipo = models.AutoField(primary_key = True)
	nombre_equipo = models.CharField(max_length=1, default='A')
	funcionario = models.ForeignKey(Especialista, null=True, blank=True, on_delete=models.CASCADE	)


=======
>>>>>>> parent of 9895f17... Creacion e implementacion de Models, Views y Urls de la aplicacion Equipo
