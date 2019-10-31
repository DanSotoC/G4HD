from django.db import models


class Archivo(models.Model):
        nombre = models.CharField(max_length= 50, default='Sin titulo')
        file = models.FileField(upload_to='archivos/')
        uploaded_at = models.DateTimeField(auto_now_add=True)
       
        def __str__(self):
        	return "{}".format(self.nombre)


 