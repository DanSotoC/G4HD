from django.shortcuts import render
from usuarios.models import Paciente, Personal
from tutor.models import Consulta

from django.contrib.auth.models import Group

def home(request):
	pacientes=Paciente.objects.count()
	personal=Personal.objects.count()
	current_user = request.user

	cont = 0
	consulta = Consulta.objects.all()
	for i in consulta:
		
		if i.estado == 0:
			cont = cont + 1

	group = Group.objects.all() 
	context = {
			'pacientes':pacientes,
			'personal':personal,
			"actual":current_user,
			"group":group,
			"consulta":cont,
	}
	return render(request,"dashboard.html", context)
