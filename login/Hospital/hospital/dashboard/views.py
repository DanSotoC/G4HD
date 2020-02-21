from django.shortcuts import render
from usuarios.models import Paciente, Personal
from django.contrib.auth.models import Group

def home(request):
	pacientes=Paciente.objects.count()
	personal=Personal.objects.count()
	current_user = request.user
	group = Group.objects.all() 
	context = {
			'pacientes':pacientes,
			'personal':personal,
			"actual":current_user,
			"group":group,
	}
	return render(request,"dashboard.html", context)
