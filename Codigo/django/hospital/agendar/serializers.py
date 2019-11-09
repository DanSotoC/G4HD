from rest_framework import serializers
from .models import DateReserva

class RutaDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = DateReserva
		fields = ['Rut','Fecha_Visita']
		read_only_fields = ()

