from django.db import models
from login.models import Usuario
from django.utils import timezone

class Paciente (models.Model):
    rut = models.ForeignKey(Usuario, null=True,  on_delete=models.CASCADE)
    hora = models.DateTimeField(null=True)
    comentario = models.CharField(max_length=90, null=True, default='')
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return  self.rut

    def publish(self):
        self.published_date = timezone.now()
        self.save()