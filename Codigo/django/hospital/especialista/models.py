from django.db import models

class ausencia:
    def __init__(self):
        id = models.IntegerField
        hora = models.DateTimeField
        comentario =models.CharField(max_length= 90)