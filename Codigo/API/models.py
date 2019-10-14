from django.db import models

class Curso(models.Model):
	sigla=models.CharField(max_length=6)
	nombre=models.CharField(max_length=60)
	creditos=models.IntegerField()

	def __str__(self):
		return "{}".format(self.nombre)

# Create your models here.
	#relaciones con tablas, revisar relaciones, not null?, iniciar como null?,

class Usuario(models.Model):
	rut_pasaporte = models.CharField(max_length=15, primary_key=True)
	nombre = models.CharField(max_length=45, null=False)
	apellido = models.CharField(max_length=45, null=False)
	telefono = models.IntegerField(null=False)
	password = models.CharField(max_length=45, null=False)
	foto = models.IntegerField()


class Externos(Usuario):
	rut_p_ex = models.OneToOneField(Usuario, parent_link=True, primary_key = True, on_delete=models.CASCADE)
	comuna = models.CharField(max_length=45, null=False)
	domicilio = models.CharField(max_length=45, null=False)
	num_domicilio = models.IntegerField(blank=True)
	num_depto = models.IntegerField(blank=True)
	edad = models.IntegerField(blank=True)
	fecha_nacimiento = models.DateTimeField(null=False)
	nacionalidad = models.CharField(max_length=10, null=False)


# persona = models.OneToOneField(Persona, parent_link=True)
# igual a = "persona_id" integer NOT NULL PRIMARY KEY REFERENCES "thread1_persona" ("id")

class Especialista(Usuario):
	rut_pasaporte_es = models.OneToOneField(Usuario, parent_link=True, primary_key=True,on_delete=models.CASCADE)
	rol = models.CharField(max_length=45, null=False)

class Rol():
	id = models.AutoField(primary_key=True)
	rol = models.CharField(max_length=20)
# Juntar con Especialistas

class Tutor(Usuario):
	rut_tutor = models.OneToOneField(Usuario, parent_link=True, on_delete=models.CASCADE)
	rut_paciente = models.CharField(max_length=15)

class Paciente(Usuario):
	rut_paciente = models.OneToOneField(Usuario, parent_link=True, primary_key=True, on_delete=models.CASCADE)
	rut_tutor = models.CharField(max_length=15)

class Ficha_medica(Paciente):
	rut = models.OneToOneField(Paciente, parent_link=True, primary_key=True, on_delete=models.CASCADE)
	nombre_paciente = models.CharField(max_length=45, null=False)
	historia = models.CharField(max_length=45)
	insumo = models.IntegerField()
	hora_inicio = models.CharField(max_length=45)
	hora_termino = models.CharField(max_length=45)
# foreign key (`Rut_pasaporte`) references `bd_hud`.`Paciente`(rut_pasaporte),


class Turnos():
	rut = models.CharField(max_length=15, primary_key=True)
	disponibilidad = models.IntegerField(null=False)
	nombre = models.CharField(max_length=45)


 # foreign key (`Rut`) references `bd_hud`.`Especialista`(rut_pasaporte),
  
class Equipo_medico():
	id = models.IntegerField(primary_key=True)
	rol = models.CharField(max_length=45)
	id_ruta = models.IntegerField()


	#  foreign key (`Rol`) references `bd_hud`.`Especialista`(`Rol`),

#class Reporte_visita():
#	rut_paciente = models.CharField(max_length=15, null=false,primary_key=true)
#	nombre_paciente = models.CharField(max_length=45, null=false)

class ruta():
	tiempo = models.DateTimeField(null=False)
	objetivo = models.CharField(max_length=45)
	id_equipo_medico = models.CharField(max_length=45, null=False, primary_key=True)

#  foreign key (`ID_equipo_medico`) references `bd_hud`.`Equipo_medico`(`id`),
  
class visita_programada(models.Model):
	id_visita = models.AutoField(primary_key=True)
	fecha = models.DateTimeField(null=False)
	eq_medico = models.IntegerField()
	rut_paciente = models.CharField(max_length=15)
	
	def __str__(self):
		return "{}".format(self.nombre)


# foreign key (`Rut_paciente`) references `bd_hud`.`Tutor`(`Rut_paciente`),
  

 #class calendario_visitas():
 #	rut_paciente = models.CharField(max_length=15, null=false,primary_key=true)
 #	fecha_inicio = models.DATE(null=false)
 #	fecha_termino = models.DATE(null=false)

 
# Primary key(`Rut_paciente`)) """ 
