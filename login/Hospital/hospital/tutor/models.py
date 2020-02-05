from django.db import models

class Consulta(models.Model):
	id_tutor = models.IntegerField()
	rut = models.CharField(null=False,max_length=20)
	mensaje = models.CharField(null=False,max_length=200)
	estado = models.CharField(null=False, default="Pendiente",max_length=20)
	respuesta = models.CharField(null=False,max_length=200, default="Sin Respuesta")


