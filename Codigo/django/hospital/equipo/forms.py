from django import forms
from .models import Crear,Registrar

class CrearForm(forms.ModelForm):
	class Meta:
		model = Crear
		fields = [
			"Nombre",
		]


class RegistrarForm(forms.ModelForm):
	class Meta:
		model = Registrar
		fields = [
			"Id",
			"Rut",
		]