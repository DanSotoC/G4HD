from django.db import models

class formulario(models.Model):
	id_visita = models.IntegerField(null=False)
	id_especialista = models.IntegerField(null=False)
	h_inicio=models.TimeField(null=False)
	h_termino=models.TimeField(null=False, auto_now_add=True)
	detalle = models.CharField(max_length=400,null=False)

