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



def Ingreso_usuarios(request,id):
	disponible=User.objects.filter(groups__name='Disponible')
	personal=Personal.objects.all()



	return render(request,"ingreso_usuarios_grupo.html",{'disponible':disponible,'personal':personal})



def Eliminar_equipo(request,id):
	group=Group.objects.get(id=id)
	if request.method=='POST':
		group.delete()
		return redirect(Listar_equipo_view)
	return render(request,"eliminar_equipo.html",{'group':group})