from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Paciente , Personal, Tutor
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
	
	if user.count() < 1:
		queryset = Personal.objects.all()
	else:
		queryset = user

	context = {

		"object_list": queryset,	
	}
	return render(request,"listen.html",context)

def usuarios_listu(request):
	qset = request.GET.get("buscar")
	user = Tutor.objects.filter(rut = qset)
	
	if user.count() < 1:
		queryset = Tutor.objects.all()
		instance = User.objects.all()
	else:
		queryset = user

	context = {

		"object_list": queryset,
		"inst": instance,	
	}
	return render(request,"listu.html",context)

