
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Perfil, Tutor
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

	
       	


def PerfilView(request):

	usuarios=User.objects.last()
	return render(request,'perfil.html',{'usuarios':usuarios})



def perfil_edit(request,usuario_id):
    usuario=Perfil.objects.get(usuario_id=usuario_id)
    if request.method=='GET':
        form=Perfil_Form(instance=usuario)
    else:
        form=Perfil_Form(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            Usuarios_in_Grupos(usuario_id)
        return redirect(PerfilView)
        
        
    return render(request,'perfil_form.html',{'form':form})	


def Registro_View(request):
	if request.method=='POST':
		form1=Registro_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

		
		return redirect(PerfilView)
	else:
		form1 = Registro_Form()
		
	return render(request,'registro.html',{'form1':form1})
			
		

def Tutor_view(request,perfil):
	
	if request.method=='POST':
		form1=Tutor_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

			
		return redirect(PerfilView)
	else:
		form1 = Tutor_Form()
		
	return render(request,'tutor_form.html',{'form1':form1, 'perfil':perfil})




def Paciente_view(request,perfil):
	tutor=Tutor.objects.get(id_perfil=perfil)
	if request.method=='POST':
		form=Paciente_Form(request.POST)
		
		

		if form.is_valid():
			form.save()

			
		return redirect(usuarios_listu)
	else:
		form = Paciente_Form()
		
	return render(request,'paciente_form.html',{'form':form, 'tutor':tutor})


def Personal_view(request,perfil):
	if request.method=='POST':
		form=Personal_Form(request.POST)
		
		

		if form.is_valid():
			form.save()

			
		return redirect(usuarios_listen)
	else:
		form = Personal_Form()
		
	return render(request,'personal_form.html',{'form':form,'perfil':perfil})

# Create your views here.
