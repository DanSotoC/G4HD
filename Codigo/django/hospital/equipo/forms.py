from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
	class Meta:
		model = Equipo
		fields = [
			"id_equipo",
			"cant_funcionarios",
		]