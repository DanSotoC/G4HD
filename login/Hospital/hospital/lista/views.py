from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Paciente


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
	user = Especialista.objects.filter(Rut = qset)
	
	if user.count() < 1:
		queryset = Especialista.objects.all()
	else:
		queryset = user

	context = {

		"object_list": queryset,	
	}
	#example of context form
	return render(request,"listen.html",context)

