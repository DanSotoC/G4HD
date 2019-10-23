from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			"Primer_Nombre",
			"Segundo_Nombre",
			"Primer_Apellido",
			"Segundo_Apellido",
			"Domicilio",
			"Comuna",
			"Telefono",
			"Rut",
			"Nacionalidad",
			"Fecha_Nacimiento",
			"Cargo",
			"Email"


		]
