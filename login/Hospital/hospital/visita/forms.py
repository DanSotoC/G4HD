from django import forms
from .models import Visita


class Agendar(forms.ModelForm):
	class Meta:
		model = Visita

		fields=['fecha',
				'id_paciente']

		widgets={

				'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
		}


class asignar_equipo(forms.ModelForm):

 	class Meta:
 		model = Visita

 		fields = [
 			'fecha',
 			'id_paciente',
 			'status',
 			'equipo'
 			]