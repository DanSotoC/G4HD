from django.shortcuts import render, get_object_or_404
from biblioteca.models import Archivo
from usuarios.models import Paciente
from usuarios.models import Tutor
from django.views.generic import TemplateView ,View

from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def logout_view(request):
    logout(request)
    return render(request,"main.html")

def home_tutor(request):
	current_user = request.user
	tx = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	

	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"email": current_user.email,
		"id_actual":current_user.id,
		"paciente": px,
		"tutor": tx,

	}
	return render(request,"home_tutor.html",context)

def biblioteca_tutor(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_tutor.html',{'archivo':archivo})


