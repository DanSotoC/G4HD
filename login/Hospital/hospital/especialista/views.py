from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from usuarios.models import Personal , Paciente, Perfil
'''from .forms import PostForm'''
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from biblioteca.models import Archivo



def logout_view(request):
    logout(request)
    return render(request,"main.html")


def home_especialista(request):
	current_user = request.user
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)

	context = {

		"actual": current_user,	
		"personal":px,

	}
	return render(request,"index_especialista.html",context)


def ver_perfil_e (request):
	current_user = request.user
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	tl = get_object_or_404(Perfil,id=current_user.id)

	context = {

		"actual": current_user,
		"personal":px,
		"tel":tl.tel,

	}
	return render(request,"ver_perfil_e.html",context)

def biblioteca_e(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_especialista.html',{'archivo':archivo})