from django.shortcuts import render
from usuarios.models import Paciente, Personal
from tutor.models import Consulta
from visita.models import Visita
from django.http import JsonResponse
from django.contrib.auth.models import Group
from datetime import datetime, date

def home(request):
	pacientes=Paciente.objects.all()
	
	pacientes_SB=Paciente.objects.filter(comuna='San Bernardo').count()
	pacientes_LP=Paciente.objects.filter(comuna='La Pintana').count()
	pacientes_EB=Paciente.objects.filter(comuna='El Bosque').count()

	personal=Personal.objects.count()
	current_user = request.user
	now = datetime.now()
	visita = Visita.objects.all()
	total = 100 #diferencia entre pacientes totales y pacientes para hoy
	hoy = 0
	completadas = 0
	SB=0
	EB=0
	LP=0
	for v in visita:
		if str(v.fecha) == str(date.today()):
			hoy = hoy + 1
			pac=Paciente.objects.get(id=v.id_paciente)
			if pac.comuna=="San Bernardo":
				SB=SB+1
			if pac.comuna=="La Pintana":
				LP=LP+1
			if pac.comuna=="El Bosque":
				EB=EB+1
			
			if v.status == 1:
				completadas = completadas + 1
			completadas = (completadas*100)/hoy


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
			'pacientes_SB':pacientes_SB,
			'pacientes_LP':pacientes_LP,
			'pacientes_EB':pacientes_EB,
			"actual":current_user,
			"group":group,
			"now":now,
			"total":total,
			"hoy":hoy,
			"realizadas":completadas,
			"SB":SB,
			"LP":LP,
			"EB":EB,

			
	}
	return render(request,"dashboard.html", context)


def get_data_consulta(request,*args,**kwargs):

	con=Consulta.objects.filter(estado='0')
	consulta=con.count()
	data={
		"consulta":consulta,
	}
	return JsonResponse(data)
	