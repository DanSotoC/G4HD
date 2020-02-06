from django.db import models

class Consulta(models.Model):
	id_tutor = models.IntegerField()
	id_usuario = models.IntegerField()
	titulo = models.CharField(null=False,max_length=20)
	rut = models.CharField(null=False,max_length=20)
	mensaje = models.CharField(null=False,max_length=200)
	estado = models.IntegerField(null=False, default=0)
	respuesta = models.CharField(null=False,max_length=200,default="Sin Respuesta")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)


