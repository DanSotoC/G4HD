from django.test import TestCase
from .models import Usuario, Especialista

class UsuarioTestCase(TestCase):

	def setUp(self):
		self.Primer_Nombre = "Prueba"
		self.Primer_Apellido = "Prueba"
		self.Segundo_Apellido = "Prueba"
		self.Telefono = "Prueba"
		self.Rut = "Prueba"
		self.Nacionalidad = "Prueba"
		self.Fecha_Nacimiento = "1960-01-01"
		self.Cargo = 1
		self.Email = "Prueba"
		self.Nombre_Completo_Tutor = "Prueba"
		self.Rut_Tutor = "Prueba"
		self.Domicilio = "Prueba"
		self.Comuna = "Prueba"
		self.usuario = Usuario(Primer_Nombre=self.Primer_Nombre,Primer_Apellido=self.Primer_Apellido,Segundo_Apellido=self.Segundo_Apellido,Telefono=self.Telefono,Rut=self.Rut,Nacionalidad=self.Nacionalidad,Fecha_Nacimiento=self.Fecha_Nacimiento,Cargo=self.Cargo, Email=self.Email, Nombre_Completo_Tutor=self.Nombre_Completo_Tutor, Rut_Tutor=self.Rut_Tutor, Domicilio=self.Domicilio,Comuna=self.Comuna)

	def test_creacion_de_usuario(self):
		old_count = Usuario.objects.count()
		self.usuario.save()
		new_count = Usuario.objects.count()
		self.assertNotEqual(old_count, new_count)


class EspecialistaTestCase(TestCase):

	def setUp(self):
		self.Primer_Nombre = "Prueba"
		self.Primer_Apellido = "Prueba"
		self.Segundo_Apellido = "Prueba"
		self.Telefono = "Prueba"
		self.Rut = "Prueba"
		self.Nacionalidad = "Prueba"
		self.Fecha_Nacimiento = "1960-01-01"
		self.Cargo = 2
		self.Email = "Prueba"
		self.especialista = Especialista(Primer_Nombre=self.Primer_Nombre,Primer_Apellido=self.Primer_Apellido,Segundo_Apellido=self.Segundo_Apellido,Telefono=self.Telefono,Rut=self.Rut,Nacionalidad=self.Nacionalidad,Fecha_Nacimiento=self.Fecha_Nacimiento, Cargo=self.Cargo, Email=self.Email)


	def test_creacion_de_especialista(self):
		old_count = Especialista.objects.count()
		self.especialista.save()
		new_count = Especialista.objects.count()
		self.assertNotEqual(old_count, new_count)