from django import forms 
from .models import Archivo


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('nombre', 'file', )

        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Inserte Nombre de Archivo'}),
        }