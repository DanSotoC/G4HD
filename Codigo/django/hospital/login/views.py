from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .models import Usuario, Especialista
from agendar.models import DateReserva
from .forms import UsuarioForm, EspecialistaForm


def usuarios_create(request):
	form = UsuarioForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.error(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {

		"form": form,
	}
	return render(request,"create_form.html",context)

def especialista_create(request):
	form = EspecialistaForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.error(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {

		"form": form,
	}
	return render(request,"especialista_form.html",context)


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

def especialista_detail(request, id=None):
	instance = get_object_or_404(Especialista, idDatosPer=id)
	context = {	
		"nom": instance.Primer_Nombre,
		"pap": instance.Primer_Apellido,
		"sap": instance.Segundo_Apellido,

		"instance": instance,
	} 
	#example of context form
	return render(request,"details.html",context)

def usuarios_listpa(request):
	queryset = Usuario.objects.all()
	context = {
		"object_list": queryset,
	}
	#example of context form
	return render(request,"listpa.html",context)

def usuarios_listen(request):
	queryset = Especialista.objects.all()
	context = {
		"object_list": queryset,
	}
	#example of context form
	return render(request,"listen.html",context)

def home_list(request):
	querysetuser = Usuario.objects.count()
	querysetesp = Especialista.objects.count()
	context = {
		"esp": querysetesp,
		"usr": querysetuser,
	}
	return render(request,"lista.html", context)

def usuarios_update(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	form = UsuarioForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
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
	messages.error(request, "Successfully deleted")
	return redirect("home_admin")

def especialista_delete(request, id=None):
	instance = get_object_or_404(Especialista, idDatosPer=id)
	instance.delete()
	messages.error(request, "Successfully deleted")
	return redirect("home_admin")

def home(request):
	return render(request,"home.html")

def asignar(request):
	return render(request,"asignar.html")

def formar(request):
	return render(request,"formar.html")

def agendar_all(request):
	instance = DateReserva.objects.all()
	context = {
		"object_list": instance,
	}
	return render(request,"agendar_lista.html", context)