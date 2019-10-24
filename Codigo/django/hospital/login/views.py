from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .models import Usuario
from .forms import UsuarioForm


def usuarios_create(request):
	form = UsuarioForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

	#	return HttpResponseRedirect(instance.get_absolute_url())


	context = {

		"form": form,
	}
	return render(request,"create_form.html",context)

def usuarios_detail(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	context = {	
		"nom": instance.Primer_Nombre,
		"pap": instance.Primer_Apellido,
		"sap": instance.Segundo_Apellido,
		"instance": instance,
	}
	#example of context form
	return render(request,"details.html",context)

def usuarios_list(request):
	queryset = Usuario.objects.all()
	context = {
		"object_list": queryset,
	}
	#example of context form
	return render(request,"index.html",context)

def usuarios_update(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	form = UsuarioForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
	#	return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")

	context = {
		"instance": instance,
		"form": form,
	}
	return render(request,"create_form.html",context)

def usuarios_delete(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	instance.delete()
	return redirect("list")

