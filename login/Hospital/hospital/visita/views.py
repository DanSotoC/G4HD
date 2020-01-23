from django.shortcuts import render, get_object_or_404
from usuarios.models import Paciente
from .forms import  Agendar

def agendar_visita(request, id=None):
	aux = get_object_or_404(Paciente, id = id)	
	form = Agendar(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
			
	context = {	

		"px": aux,
		"form":form,
	}
	return render(request,"agendar_visita.html",context)
	

