from django.shortcuts import render, get_object_or_404,redirect
from usuarios.models import Paciente
from visita.models import Visita
from usuarios.models import Tutor
from usuarios.models import Perfil
from .forms import  Agendar
from lista.views import usuarios_listpa
from django.contrib import messages
from django.contrib.auth.models import User

def agendar_visita(request, id=None):
	aux = Paciente.objects.get(id=id)	
	form=Agendar(request.POST)
	if request.method=='POST':
		
		if form.is_valid():
			form.save()

			
		return redirect(visita_paciente_admin,id)
	else:
		form = Agendar()
	return render(request,"agendar_visita.html",{"form":form,"px":aux})

def agendar_lista(request):
	queryset = Visita.objects.all()
	instance = Paciente.objects.all()


	context = {

		"date_list": queryset,
		"px": instance,


	}	

	return render(request,"agendar_lista.html",context)
	
def visita_paciente(request):
	queryset = Visita.objects.all()
	current_user = request.user
	px = Paciente.objects.all()
	instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)



	context = {

		"date_list": queryset,
		"px": px,
		"aux":instance.id,
	}	

	return render(request,"visita_paciente.html",context)

def visita_paciente_admin(request, id=None):
	px = Paciente.objects.get(id=id)
	queryset = Visita.objects.all()
	tx = Tutor.objects.get(id=px.id_tutor_id)
	usr = get_object_or_404(User, id=tx.id_perfil_id)
	tel = get_object_or_404(Perfil, id=tx.id_perfil_id)

	context = {

		"date_list": queryset,
		"obj": px,
		"usr":usr,
		"tx":tx,
		"tel":tel,


	}	

	return render(request,"registro_visita_adm.html",context)


def borrar_fecha(request,id=None):
	instance = get_object_or_404(Visita, id=id)
	id_p=instance.id_paciente
	instance.delete()
	messages.error(request, "Successfully deleted")
	return redirect(visita_paciente_admin,id_p)






def visita_update(request, id=None):
	aux = Visita.objects.get(id=id)	
	
	if request.method=='GET':
		form=Agendar(instance=aux)
	else:
		form=Agendar(request.POST,instance=aux)		
		if form.is_valid():
			form.save()
		return redirect(agendar_lista)
	
	return render(request,"agendar_update.html",{"form":form,"id_paciente":aux.id_paciente,"status":aux.status})

def reagendar(request):
	return render(request,"reagendar.html")


def visita_paciente_detalle(request, id=None):
	queryset = get_object_or_404(Visita, id=id)

	context = {

		"visita": queryset,
		
	}	

	return render(request,"visita_paciente_detalle.html",context)