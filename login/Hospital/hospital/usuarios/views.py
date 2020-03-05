
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Perfil, Tutor, Paciente ,Personal
from .forms import  Registro_Form,Perfil_Form, Tutor_Form, Paciente_Form, Personal_Form
from django.urls import reverse_lazy
import threading
from django.contrib.auth.models import Group
from lista.views import usuarios_listen, usuarios_listu
from django.contrib.auth.decorators import login_required

def Usuarios_in_Grupos(usuario_id):
	users=User.objects.get(id=usuario_id)
	tutores=Group.objects.get(name='Tutores')
	personal=Group.objects.get(name='Personal')
	disponible=Group.objects.get(name='Disponible')

	if users.perfil.rol=='TUTOR':
		tutores.user_set.add(users)
	else:
		if users.perfil.rol=='PERSONAL':
			personal.user_set.add(users)
			disponible.user_set.add(users)


def Set_password(usuario_id):
	nombre=[]
	apellido=[]
	tel=[]
	clave=[]
	user=User.objects.get(id=usuario_id)
	perfil=Perfil.objects.get(id=usuario_id)
	nombre=user.first_name
	apellido=user.last_name
	tel=perfil.tel
	clave.append(nombre[:3])
	clave.append(apellido[:3])
	clave.append(tel[:4])
	user.set_password(clave[0].lower()+clave[1].lower()+clave[2])
	user.save()


	
       	


def PerfilView(request,perfil):
	tutor=None
	paciente=None
	personal=None
	usuario=User.objects.get(id=perfil)
	perfile=Perfil.objects.get(id=perfil)
	if perfile.rol=='TUTOR':
		tutor=Tutor.objects.get(id_perfil=perfil)
		paciente=Paciente.objects.get(id_tutor=tutor.id)
	if perfile.rol=='PERSONAL':
		personal=Personal.objects.get(id_perfil=perfil)
	
	context={
		"usuario":usuario,
		"perfil":perfile,
		"tutor":tutor,
		"personal":personal,
		"paciente":paciente
	}

	return render(request,'perfil.html',context)



def perfil_edit(request,usuario_id):
    usuario=Perfil.objects.get(usuario_id=usuario_id)
    if request.method=='GET':
        form=Perfil_Form(instance=usuario)
    else:
        form=Perfil_Form(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            Usuarios_in_Grupos(usuario_id)
            Set_password(usuario_id)
        if usuario.rol=='TUTOR':
        	return redirect(Tutor_view,usuario.id)
        if usuario.rol=='PERSONAL':
        	return redirect(Personal_view,usuario.id)
        
        
    return render(request,'perfil_form.html',{'form':form})	


def Registro_View(request):
	if request.method=='POST':
		form1=Registro_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

		usuarios=User.objects.last()
		usuario_id=usuarios.id
		return redirect(perfil_edit,usuario_id)
	else:
		form1 = Registro_Form()
		
	return render(request,'registro.html',{'form1':form1})
			
		

def Tutor_view(request,perfil):
	
	if request.method=='POST':
		form1=Tutor_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

			
		return redirect(Paciente_view,perfil)
	else:
		form1 = Tutor_Form()
		
	return render(request,'tutor_form.html',{'form1':form1, 'perfil':perfil})




def Paciente_view(request,perfil):
	tutor=Tutor.objects.get(id_perfil=perfil)
	if request.method=='POST':
		form=Paciente_Form(request.POST)
		
		

		if form.is_valid():
			form.save()

			
		return redirect(PerfilView,perfil)
	else:
		form = Paciente_Form()
		
	return render(request,'paciente_form.html',{'form':form, 'tutor':tutor})






def Personal_view(request,perfil):
	if request.method=='POST':
		form=Personal_Form(request.POST,request.FILES)
		
		

		if form.is_valid():
			form.save()

			
		return redirect(PerfilView,perfil)
	else:
		form = Personal_Form()
		
	return render(request,'personal_form.html',{'form':form,'perfil':perfil})

# Create your views here.
