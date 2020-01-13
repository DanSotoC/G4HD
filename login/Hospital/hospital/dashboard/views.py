from django.shortcuts import render
from usuarios.models import Paciente, Personal

def home(request):
	pacientes=Paciente.objects.count()
	personal=Personal.objects.count()
	context = {
			'pacientes':pacientes,
			'personal':personal
	}
	return render(request,"dashboard.html", context)
