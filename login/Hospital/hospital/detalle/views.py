from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente
from usuarios.models import Tutor


def usuario_detail(request, id=None):
	px = get_object_or_404(Paciente, id_tutor_id=id)
	tx = get_object_or_404(Tutor, id=id)
	context = {	
		"paciente":px,
		"tutor": tx,
	} 
	return render(request,"details.html",context)
