
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Perfil, Tutor
from .forms import  Registro_Form,Perfil_Form, Tutor_Form, Paciente_Form
from django.urls import reverse_lazy
import threading




def PerfilView(request):

	usuarios=User.objects.last()
	
	return 	render(request,'perfil.html',{'usuarios':usuarios})



def perfil_edit(request,usuario_id):
    usuario=Perfil.objects.get(usuario_id=usuario_id)
    if request.method=='GET':
        form=Perfil_Form(instance=usuario)
    else:
        form=Perfil_Form(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
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
			
		

def Tutor_view(request):
	usuarios=User.objects.last()
	if request.method=='POST':
		form1=Tutor_Form(request.POST)
		
		

		if form1.is_valid():
			form1.save()

			
		return redirect(PerfilView)
	else:
		form1 = Tutor_Form()
		
	return render(request,'tutor_form.html',{'form1':form1,'usuarios':usuarios})



def Paciente_view(request):
	if request.method=='POST':
		form=Paciente_Form(request.POST)
		
		

		if form.is_valid():
			form.save()

			
		return redirect(PerfilView)
	else:
		form = Paciente_Form()
		
	return render(request,'paciente_form.html',{'form':form})



# Create your views here.
