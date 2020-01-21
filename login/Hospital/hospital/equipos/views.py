from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from usuarios.models import Personal, Perfil
from django.contrib.auth.models import User

# Create your views here.



def Crear_equipo_view(request):
	if request.POST.get('nombre_equipo'):
		nombre=request.POST.get('nombre_equipo')
		group = Group.objects.create(name=nombre)
		group.save()
		return redirect(Listar_equipo_view)
	else:
		return render(request,'crear_equipo.html')
	return render(request,'crear_equipo.html')

def Listar_equipo_view(request):

	group = Group.objects.all()

	return render(request,'listar_equipo.html',{'group':group})




def Asignar_equipo_view(request):
	
	personal=Personal.objects.all()
	group = Group.objects.all()


	return render(request,'asignar_equipo.html',{'personal':personal,'group':group})



def Ingreso_usuarios(request,):
	'''disponible=Group.objects.get(id=8)
	personal=User.group.get(id=8)'''
	return render(request,"ingreso_usuarios_grupo.html",context=None)