from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Paciente , Personal, Tutor
from tutor.models import Consulta
from .forms import Paciente_Form_activo

from django.contrib.auth.models import User
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return render(request,"main.html")

def usuarios_listpa(request):
	qset = request.GET.get("buscar")
	user = Paciente.objects.filter(rut = qset)
	current_user = request.user

	if user.count() < 1:
		queryset = Paciente.objects.all()
	else:
		queryset = user	
	
	context = {

		"object_list": queryset,
		"actual":current_user,

	}
	return render(request,"listpa.html",context)


def usuarios_listen(request):
	qset = request.GET.get("buscar")
	user = Personal.objects.filter(rut = qset)
	current_user = request.user
	
	if user.count() < 1:
		queryset = Personal.objects.all()
	else:
		queryset = user

	context = {

		"object_list": queryset,
		"actual":current_user,	
	}
	return render(request,"listen.html",context)

def usuarios_listu(request):
	qset = request.GET.get("buscar")
	user = Tutor.objects.filter(rut = qset)
	current_user = request.user
	
	if user.count() < 1:
		queryset = Tutor.objects.all()
		instance = User.objects.all()
	else:
		queryset = user

	context = {

		"object_list": queryset,
		"inst": instance,	
		"actual":current_user,
	}
	return render(request,"listu.html",context)

def consulta_lista(request):
	
	con = Consulta.objects.all().order_by('timestamp')
	usr = User.objects.all()
	var = 0

	context = {

		"con": con,
		"usr": usr,
		"var":var,
	}
	return render(request,"consulta_lista.html",context)


def reingreso(request):
	qset = request.GET.get("buscar")
	user = Paciente.objects.filter(rut = qset)
	calificacion = 4

	if user.count() < 1:
		queryset = Paciente.objects.all()
	else:
		queryset = user

	context = {
		"object_list":queryset,
		"nota":calificacion,
	}
	return render(request,"reingreso.html",context)


def reingreso_paciente(request, id=None):
	instance = get_object_or_404(Paciente, id=id)
	episodio = instance.episodio + 1
	

	if request.method=='GET':
		form=Paciente_Form_activo(instance=instance)
	else:
		form=Paciente_Form_activo(request.POST,instance=instance)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('listpaciente'))

	context = {

		"paciente":instance,
		"form":form,
		"ep":episodio,
		

	}

	return render(request,"confirmarreingreso.html",context)





