from rest_framework import serializers
from .models import Curso



class CursoSerializer(serializers.ModelSerializer):
	"""Serializador para mapear un curso a formato JSON."""

	class Meta:
		"""Meta clase para el mapeo de atributos."""
		model = Curso
		fields = ('id','sigla','nombre','creditos')
		read_only_fields = ()


from .models import visita_programada

class RutaDataSerializer(serializers.ModelSerializer):

	class Test:
		"""Serializer de prueba"""
		model = visita_programada
		fields = ('id_visita','fecha', 'eq_medico', 'rut_paciente')
		read_only_fields = ()

