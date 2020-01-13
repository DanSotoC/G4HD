from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil , Tutor , Paciente
from django.contrib.auth.models import User


class Registro_Form(UserCreationForm):
 	first_name = forms.CharField(max_length=140, required = True)
 	last_name = forms.CharField(max_length=140, required=False)
 	email = forms.EmailField(required=True)
 	
 	class Meta:
 		model = User

 		fields = (
 			'username',
 			'email',
 			'first_name',
 			'last_name',
 			'password1',
 			'password2'
 			)
 		
 

		



class Perfil_Form(forms.ModelForm):
	class Meta:
		ROL=(
			('PERSONAL','Personal'),
			('TUTOR','Tutor'))

		model = Perfil

		fields=['rol',
				'tel',]



		widgets={
		'rut':forms.TextInput(attrs={'class':'form-control','placeholder':'12.345.68-9'}),
		'rol':forms.Select(choices=ROL,attrs={'class':'form-control'}),
		'tel':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese número telefónico '})
		}


class Tutor_Form(forms.ModelForm):
	class Meta:
		model = Tutor

		fields=['id_perfil','rut',
				'comuna',
				'domicilio',
				'num_domicilio',
				'edad',
				'f_nacimiento']


class Paciente_Form(forms.ModelForm):
	class Meta:
		model = Paciente

		fields=['id_tutor',
				'nombre',
				'apellido1',
				'apellido2',
				'rut',
				'comuna',
				'domicilio',
				'num_domicilio',
				'edad_paciente',
				'f_nacimiento',
				'desc']