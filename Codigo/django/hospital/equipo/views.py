<<<<<<< HEAD
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .models import Equipo
from .forms import EquipoForm


def crear(request):
	form = EquipoForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("crear")
	context = {

		"form": form,
	}

	return render(request,"crear_equipo.html",context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> parent of 9895f17... Creacion e implementacion de Models, Views y Urls de la aplicacion Equipo
