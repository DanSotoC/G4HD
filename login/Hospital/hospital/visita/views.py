from django.shortcuts import render, get_object_or_404,redirect
from usuarios.models import Paciente
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

	

