from django.test import TestCase
from .models import DateReserva

class ReservaTestCase(TestCase):

	def setUp(self):
		self.Rut = "Prueba"
		self.Fecha_Visita = "1990-01-01"
		self.Latitud = "Prueba"
		self.Longitud = "Prueba"
		self.reserva = DateReserva(Rut=self.Rut,Fecha_Visita=self.Fecha_Visita, Latitud=self.Latitud, Longitud=self.Longitud)

	def test_creacion_de_reserva(self):
		old_count = DateReserva.objects.count()
		self.reserva.save()
		new_count = DateReserva.objects.count()
		self.assertNotEqual(old_count, new_count)



