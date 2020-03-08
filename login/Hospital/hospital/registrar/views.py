from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from usuarios.models import Paciente, Personal
from usuarios.models import Tutor
from usuarios.models import Perfil
from visita.models import Visita
from django.contrib.auth.models import User
from registrar.forms import formulario_visita_esp
from especialista.views import visitas_programadas_esp
from visita.forms import  asignar_equipo
from datetime import date, time,datetime
from registrar.models import formulario as fm

def formulario(request, id=None):

	now = datetime. now()
	current_time = now. strftime("%H:%M:%S")
	now=datetime.today()
	current_user = request.user
	personal=Personal.objects.get(id_perfil=current_user.id)
	visita =  get_object_or_404(Visita, id=id)
	px = get_object_or_404(Paciente, id=visita.id_paciente)
	form=formulario_visita_esp(request.POST)
	if request.method=='POST':
		form=formulario_visita_esp(request.POST)




		if form.is_valid():
			visita.status=1
			visita.save()
			form.save()

			return redirect(visitas_programadas_esp)
	context = {

		"id_visita": visita.id,
		"id_especialista": personal.id,
		"actual":current_user,
		"px":px,
		"form":form,
		"h_inicio":current_time,
		"id_paciente":px.id,
	}
		
	return render(request,'formulario_visita_esp.html',context)


def ver_formulario(request, id=None):

	visita = get_object_or_404(Visita, id=id)
	frml = get_object_or_404(fm,id_visita=visita.id)
	


	context = {

		"f": frml,
		"v": visita,
	}

	return render(request,'ver_formulario_detalle.html',context)


def ver_registro_admin(request, id=None):

	px = get_object_or_404(Paciente, id=id)
	fx = Visita.objects.all()


	context = {

		"obj":px,
		"date_list":fx,
		"episodio": range(1,px.episodio+1),
		"count": 1,

	}


	return render(request,'ver_registro_admin.html',context)