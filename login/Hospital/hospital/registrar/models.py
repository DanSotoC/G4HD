from django.db import models

class formulario(models.Model):
	id_fecha = models.IntegerField(null=False)
	id_especialista = models.IntegerField(null=False)
	detalle = models.CharField(max_length=400,null=False)

