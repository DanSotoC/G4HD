from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import formulario


class formulario_visita_esp(forms.ModelForm):

 	class Meta:
 		model = formulario

 		fields = [
 			'id_fecha',
 			'id_especialista',
 			'detalle'
 			]
