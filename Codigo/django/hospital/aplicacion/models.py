from django.db import models

class Datos_Personales(models.Model):
	id_datos_personales = models.IntegerField(primary_key = True)
	primer_nombre = models.CharField(max_length = 15)
	segundo_nombre = models.CharField(max_length = 15)
	primer_apellido = models.CharField(max_length = 15)
	segundo_apellido = models.CharField(max_length = 15)
	domicilio = models.CharField(max_length = 40)
	telefono = models.CharField(max_length = 15)
	rut = models.CharField(max_length = 15)
	nacionalidad = models.CharField(max_length = 30)
	fecha_nacimiento = models.DateField()
	comuna = models.CharField(max_length = 30)
	#foto = models.ImageField()#upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg'


class Usuario(models.Model):
	id_usuario = models.IntegerField(primary_key = True)
	cargo = models.CharField(max_length = 10)
	mail = models.CharField(max_length = 100)
	id_datos_personales = models.OneToOneField(Datos_Personales, null=True, blank=True, on_delete=models.CASCADE) 


class Cuidador(models.Model):
	id_cuidador = models.IntegerField(primary_key = True)
	parentezco = models.CharField(max_length = 10)
	id_usuario = models.OneToOneField(Datos_Personales, null=True, blank=True, on_delete=models.CASCADE)


class Ruta(models.Model):
	id_ruta = models.IntegerField(primary_key = True)
	Hora_Inicio = models.TimeField()
	Hora_Fin = models.TimeField()
	fecha_ruta = models.DateField()


class Equipo(models.Model):
	id_ruta = models.OneToOneField(Ruta, null=True, blank=True, on_delete=models.CASCADE) 
	id_usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE) 


class Biblioteca(models.Model):
	id_biblioteca = models.IntegerField(primary_key = True)
	contacto_hospital = models.CharField(max_length = 11)


class Calendario_Visita(models.Model):
	id_cuidador = models.OneToOneField(Cuidador, null=True, blank=True, on_delete=models.CASCADE) 
	Fecah_Calendario = models.DateField()


class Paciente(models.Model):
	id_paciente = models.IntegerField(primary_key = True)
	id_cuidador = models.OneToOneField(Cuidador, null=True, blank=True, on_delete=models.CASCADE) 
	estado = models.CharField(max_length = 20)


#class Visita(models.Model):
#    id_Visita = models.IntegerField(max_length = 11, primary_key = True)

		
