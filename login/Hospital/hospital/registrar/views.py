from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Perfil
from visita.models import Visita
from django.contrib.auth.models import User
from registrar.forms import formulario_visita_esp

def formulario(request, id=None):
	current_user = request.user
	visita =  get_object_or_404(Visita, id=id)
	px = get_object_or_404(Paciente, id=visita.id_paciente)
	
	form = formulario_visita_esp(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('home_e'))

	context = {

		"id_visita": visita.id,
		"id_paciente": visita.id_paciente,
		"actual":current_user,
		"px":px,
	}
		
	return render(request,'formulario_visita_esp.html',context)
