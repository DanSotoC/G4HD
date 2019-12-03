from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .models import Crear,Registrar
from .forms import CrearForm,RegistrarForm


def crear_equipo(request):
	form = CrearForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("crear_equipo")
	context = {

		"form": form,
	}

	return render(request,"crear_equipo.html",context)


def registrar_funcionario(request):
	form = RegistrarForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("registrar_funcionario")
	context = {

		"form": form,
	}

	return render(request,"registrar_funcionario.html",context)


def listar_equipos(request, id=None):
	queryset = Registrar.objects.all()
	
	context = {

		"object_list": queryset,	
	}
	return render(request,"listar_equipo.html",context)