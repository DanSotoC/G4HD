from django.db import models

class Visita(models.Model):
	fecha = models.DateField(null=False)
	id_paciente = models.IntegerField(null=False)
	status = models.IntegerField(null=False, default=0) #0 = Activa 1= Completa 
	equipo = models.CharField(max_length=20,null=False, default='Disponible') #0 = ninguno otro= id_equipo
	episodio = models.IntegerField(null=False, default=0)

class Tiempos(models.Model):
	item = models.CharField(max_length=20,null=False)
	tiempo = models.IntegerField(null=False, default=0)


class Llamar(models.Model):
	tel = models.CharField(max_length=20,null=False)
	correo = models.CharField(max_length=40,null=False)
	texto_explicativo = models.CharField(max_length=200,null=False)
