from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Consulta


class consulta_mensaje(forms.ModelForm):

 	class Meta:
 		model = Consulta

 		fields = [
 			'id_tutor',
 			'rut',
 			'mensaje',
 			'estado',
 			'respuesta'
 			]
