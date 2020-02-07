from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from usuarios.models import Personal , Paciente, Perfil
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from biblioteca.models import Archivo
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


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
	group=Group.objects.all()
	for g in group:
		if g.id != '1' and g.id != '2' and g.id != '20':
			user=User.objects.filter(groups__id=g.id)
			for u in user:
				if u.id == current_user.id:
					name=g.name
					user_group=User.objects.filter(groups__name=name)

	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	tl = get_object_or_404(Perfil,id=current_user.id)
	

	context = {

		"actual": current_user,
		"personal":px,
		"tel":tl.tel,
		"users_group":user_group,
		"name_group":name

	}
	return render(request,"ver_perfil_e.html",context)

def biblioteca_e(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_especialista.html',{'archivo':archivo})


def Especialista_edit(request,perfil=None,id_personal=None):
	
	personal=Personal.objects.get(id=id_personal)
	if request.method=='GET':
		form=Personal_Form(instance=personal)
	else:
		form=Personal_Form(request.POST,instance=personal)
		if form.is_valid():
			form.save()
		return redirect(ver_perfil_e)
	return render(request,'personal_f.html',{'form':form,'perfil':perfil})


def contraseña_edit(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Tu password ha sido cambiada exitosamente!')
			return redirect(contraseña_edit)
		else:
			messages.error(request, 'Porfavor ingrese clave correcta')
			return redirect(contraseña_edit)
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'contra_especialista_edit.html',{'form': form})
		