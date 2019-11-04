from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from login.models import Usuario

def home_especialista(request):
	return render(request,"index_especialista.html")

def ausencia_paciente(request):
	queryset =request.GET.get("buscar")
	context = {
		"object_list": queryset,
	}
	return render(request, "ausencia_paciente.html", context)


def ausencia_paciente_detalle(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	context = {
		"nom": instance.Primer_Nombre,
		"snom": instance.Segundo_Nombre,
		"pap": instance.Primer_Apellido,
		"sap": instance.Segundo_Apellido,

		"instance": instance,
	}
	return render(request,"ausencia_paciente_detalle.html", context)