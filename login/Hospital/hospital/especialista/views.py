from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

'''from .forms import PostForm'''
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages


def home_especialista(request):
	return render(request,"index_especialista.html")

def ausencia_paciente(request):
	queryset =request.GET.get("buscar")
	user = Usuario.objects.filter(Rut = queryset)
	context = {
		"object_list": user,
	}
	return render(request, "ausencia_paciente.html", context)


def ausencia_paciente_detalle(request, id =None):
	instance = get_object_or_404(Usuario, idDatosPer = id)
	context = {
		"nom": instance.Primer_Nombre,
		"pap": instance.Primer_Apellido,
		"sap": instance.Segundo_Apellido,

		"instance": instance,
	}
	return render(request,"ausencia_paciente_detalle.html", context)

def ausencia_paciente_form(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	form = PostForm(request.POST or None)

	if form.is_valid():
		print("dentro")
		inst = form.save(commit=False)
		inst.save()
		messages.error(request, "Successfully Created")
#		return HttpResponseRedirect(instance.get_absolute_url())
		return HttpResponseRedirect("ausencia_paciente_detalle.html")
	else :
		print(form)

	context = {

		"form": form,
		"instance": instance,
	}
	return render(request, "ausencia_paciente_form.html", context)
