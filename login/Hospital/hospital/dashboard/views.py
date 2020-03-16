from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente, Personal
from tutor.models import Consulta
from visita.models import Visita, Tiempos
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

	if hoy == 0:
		completadas = 100
	else:
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
	


def equipo_dash(request,id=None):

	group = get_object_or_404(Group, id=id)
	px = Paciente.objects.all()
	vx = Visita.objects.all()
	tx = Tiempos.objects.all()

	aux = 0
	cont = 0
	tiempo = 0
	taux = 0
	horas = 0
	minutos = 0

	for v in vx:
		if str(v.fecha) == str(date.today()): 
			if v.equipo == group.name:
				cont = cont + 1 #Total de visitas del equipo
				
				if v.status == 1:
					aux = aux +1 #Visitas completadas
				else:
					p = get_object_or_404(Paciente, id=v.id_paciente)
					for i in tx:
						if i.item == p.tipo:
							tiempo = tiempo + i.tiempo
							taux = taux + 1


	if tiempo != 0:
		horas = tiempo/60
		horas = int(horas)
		minutos = tiempo - (horas*60)


	context = {

		"group":group.name,
		"totalvisitas": cont,
		"realizadas": aux,
		"horas": horas,
		"minutos": minutos,
		"t":tiempo,
		"vx":vx,
		"px":px,
		"hoy":str(date.today()),

	}

	return render(request,"equipo_detalle_dash.html",context)