from django.shortcuts import render
from django.contrib.auth.models import Group

# Create your views here.



def Crear_equipo_view(request):
	if request.POST.get('nombre_equipo'):
		nombre=request.POST.get('nombre_equipo')
		group = Group.objects.create(name=nombre)
		group.save()
		return render(request,'listar_equipo.html')
	else:
		return render(request,'crear_equipo.html')
	return render(request,'crear_equipo.html')

def Listar_equipo_view(request):

	return render(request,'listar_equipo.html')




def Asignar_equipo_view(request):

	return render(request,'asignar_equipo.html')