from django.shortcuts import render
from usuarios.models import Paciente, Personal
from tutor.models import Consulta
from django.http import JsonResponse
from django.contrib.auth.models import Group
from datetime import datetime

def home(request):
	pacientes=Paciente.objects.all()
	personal=Personal.objects.count()
	current_user = request.user
	now = datetime.now()
	total = 100 #diferencia entre pacientes totales y pacientes para hoy

	aux = 0
	for n in pacientes:
		if n.activo == 1:
			aux = aux + 1



	cont = 0
	consulta = Consulta.objects.all()
	for i in consulta:
		
		if i.estado == 0:
			cont = cont + 1

	group = Group.objects.all() 
	context = {
			'pacientes':aux,
			'personal':personal,
			"actual":current_user,
			"group":group,
			"now":now,
			"total":total,
			
	}
	return render(request,"dashboard.html", context)


def get_data_consulta(request,*args,**kwargs):

	con=Consulta.objects.filter(estado='0')
	consulta=con.count()
	data={
		"consulta":consulta,
	}
	return JsonResponse(data)
	