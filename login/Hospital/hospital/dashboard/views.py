from django.shortcuts import render
from usuarios.models import Paciente, Personal

def home(request):
	pacientes=Paciente.objects.count()
	personal=Personal.objects.count()
	current_user = request.user
	context = {
			'pacientes':pacientes,
			'personal':personal,
			"actual":current_user,
	}
	return render(request,"dashboard.html", context)
