from django import forms
from .models import DateReserva

class AgendarForm(forms.ModelForm):
	class Meta:
		model = DateReserva
		fields = [
			"Id",
			"Rut",
			"Fecha_Visita"
		]
		