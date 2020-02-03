from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Personal
from usuarios.models import Perfil
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from lista.views import usuarios_listpa


def borrar_paciente(request,id):
	obj = get_object_or_404(User, id=id)
	if request.method=="POST":
		obj.delete()
		return redirect("/dashboard/home/")
	context = {	
	  "object":obj
	} 
	return render(request,"delete.html",context)

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


def paciente_edit(request,id_tutor=None,id_paciente=None):
	paciente=Paciente.objects.get(id=id_paciente)
	tutor=Tutor.objects.get(id=id_tutor)
	if request.method=='GET':
		form=Paciente_Form(instance=paciente)
	else:
		form=Paciente_Form(request.POST,instance=paciente)
		if form.is_valid():
			form.save()
		return redirect(usuario_detail,id_paciente)
	return render(request,'paciente_form.html',{'form':form,'tutor':tutor})	


def tutor_edit(request,perfil=None,id_detalle=None):
	
	tutor=Tutor.objects.get(id=id_detalle)
	if request.method=='GET':
		form1=Tutor_Form(instance=tutor)
	else:
		form1=Tutor_Form(request.POST,instance=tutor)
		if form1.is_valid():
			form1.save()
		return redirect(tutor_detail,perfil)
	return render(request,'tutor_form.html',{'form1':form1,'perfil':perfil})


def especialista_edit(request,perfil=None,id_personal=None):
	
	personal=Personal.objects.get(id=id_personal)
	if request.method=='GET':
		form=Personal_Form(instance=personal)
	else:
		form=Personal_Form(request.POST,instance=personal)
		if form.is_valid():
			form.save()
		return redirect(especialista_detail,id_personal)
	return render(request,'personal_form.html',{'form':form,'perfil':perfil})







