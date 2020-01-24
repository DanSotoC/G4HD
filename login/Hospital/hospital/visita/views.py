from django.shortcuts import render, get_object_or_404,redirect
from usuarios.models import Paciente
from visita.models import Visita
from usuarios.models import Tutor
from .forms import  Agendar
from lista.views import usuarios_listpa

def agendar_visita(request, id=None):
	aux = Paciente.objects.get(id=id)	
	form=Agendar(request.POST)
	if request.method=='POST':
		
		if form.is_valid():
			form.save()

			
		return redirect(usuarios_listpa)
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