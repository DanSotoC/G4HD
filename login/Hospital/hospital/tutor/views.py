from django.shortcuts import render, get_object_or_404, redirect
from biblioteca.models import Archivo
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Perfil
from django.contrib.auth.models import User
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from django.views.generic import TemplateView ,View
from tutor.forms import consulta_mensaje
from tutor.models import Consulta

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
		"actual":current_user,

	}
	return render(request,"home_tutor.html",context)

def ver_perfil (request):
	current_user = request.user
	tx = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	tl = get_object_or_404(Perfil,id=current_user.id)

	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"email": current_user.email,
		"id_actual":current_user.id,
		"paciente": px,
		"tutor": tx,
		"actual":current_user,
		"tel":tl.tel,
		"usr":tl

	}
	return render(request,"ver_perfil.html",context)

def biblioteca_tutor(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_tutor.html',{'archivo':archivo})


def Tutor_edit(request,perfil=None,id_detalle=None):
	
	tutor=Tutor.objects.get(id=id_detalle)
	if request.method=='GET':
		form1=Tutor_Form(instance=tutor)
	else:
		form1=Tutor_Form(request.POST,instance=tutor)
		if form1.is_valid():
			form1.save()
		return redirect(ver_perfil)
	return render(request,'tutor_f.html',{'form1':form1,'perfil':perfil,'tutor':tutor})


def Paciente_edit(request,id_tutor=None,id_paciente=None):
	paciente=Paciente.objects.get(id=id_paciente)
	tutor=Tutor.objects.get(id=id_tutor)
	if request.method=='GET':
		form=Paciente_Form(instance=paciente)
	else:
		form=Paciente_Form(request.POST,instance=paciente)
		if form.is_valid():
			form.save()
		return redirect(ver_perfil)
	return render(request,'paciente_f.html',{'form':form,'tutor':tutor,'paciente':paciente})	


def contacto(request):
	current_user = request.user
	tx =  get_object_or_404(Tutor, id_perfil_id = current_user.id)
	

	form = consulta_mensaje(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect(ver_perfil)

	context = {

		"form": form,
		"user": tx,
		"actual":current_user,
	}
		
	return render(request,'Contacto.html',context)

def ver_consultas (request):
	current_user = request.user
	tx = Tutor.objects.all()
	con = Consulta.objects.all()

	context = {

		"tutor": tx,
		"actual":current_user,
		"con":con,
		"aux":current_user.id,


	}
	return render(request,"ver_consulta.html",context)

def ver_respuesta (request,id=None):
	current_user = request.user
	con =  get_object_or_404(Consulta, id=id)

	context = {

		"actual":current_user,
		"con":con,

	}
	return render(request,"ver_respuesta.html",context)
