from django.db import models

class Paciente:
    def __init__(self):
        rut = models.CharField(max_length=12)
        hora = models.DateTimeField
        comentario =models.CharField(max_length= 90)

    def __str__(self):
        return  self.rut