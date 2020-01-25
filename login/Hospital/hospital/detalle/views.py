from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Personal
from usuarios.models import Perfil


def usuario_detail(request, id=None):
	px = get_object_or_404(Paciente, id_tutor_id=id)
	tx = get_object_or_404(Tutor, id=id)
	current_user = request.user
	context = {	
		"paciente":px,
		"tutor": tx,
		"actual":current_user,
	} 
	return render(request,"detailspaciente.html",context)

def tutor_detail(request, id=None):
	instance = get_object_or_404(User, id=id)
	detalle = get_object_or_404(Tutor, id_perfil_id=id)
	current_user = request.user

	context = {	
	
		"usr":instance,
		"det":detalle,
		"actual":current_user,
	} 
	return render(request,"detailstutor.html",context)

def especialista_detail(request, id=None):
	detalle = get_object_or_404(Personal, id=id)
	instance = get_object_or_404(User, id=detalle.id_perfil_id)
	current_user = request.user

	context = {	
	
		"usr":instance,
		"det":detalle,
		"actual":current_user,
	} 
	return render(request,"detailspersonal.html",context)


