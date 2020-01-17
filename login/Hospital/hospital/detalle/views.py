from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from usuarios.models import Paciente
from usuarios.models import Tutor


def usuario_detail(request, id=None):
	px = get_object_or_404(Paciente, id_tutor_id=id)
	tx = get_object_or_404(Tutor, id=id)
	context = {	
		"paciente":px,
		"tutor": tx,
	} 
	return render(request,"detailspaciente.html",context)

def tutor_detail(request, id=None):
	instance = get_object_or_404(User, id=id)
	detalle = get_object_or_404(Tutor, id_perfil_id=id)

	context = {	
	
		"usr":instance,
		"det":detalle,
	} 
	return render(request,"detailstutor.html",context)