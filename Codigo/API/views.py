from django.shortcuts import render

from rest_framework import generics
from .serializers import CursoSerializer
from .models import Curso


from .models import visita_programada
from .serializers import RutaDataSerializer

class CreateView(generics.ListCreateAPIView):
	"""Vista que representa el comportamiento de la API REST"""
	#El  queryset contiene la coleccion de todos los cursos 
	queryset = visita_programada.objects.all()
	serializer_class = RutaDataSerializer

	def perform_create(self, serializer):
		"""Almacena los datos recibidos mediante POST como un curso"""
		serializer.save()

# Create your views here.

class TestView(generics.ListCreateAPIView):
	queryset = visita_programada.objects.all()
	serializer_class = RutaDataSerializer

	def perform_create(self, serializer):
		"""Almacena los datos recibidos mediante POST como un curso"""
		serializer.save()


"""

class CreateView(generics.ListCreateAPIView):
	#Vista que representa el comportamiento de la API REST
	#El  queryset contiene la coleccion de todos los cursos 
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer

	def perform_create(self, serializer):
		#Almacena los datos recibidos mediante POST como un curso
		serializer.save() 
"""

