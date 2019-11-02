from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .models import Equipo, Asignar
from .forms import EquipoForm


def crear(request):
	form = EquipoForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.error(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {

		"form": form,
	}

	return render(request,"crear_equipo.html",context)