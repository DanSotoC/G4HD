from django.shortcuts import render
from .models import Usuario
from .forms import AgendarForm

def agendar_usuario(request):
	form = AgendarForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("agendar")
	context = {

		"form": form,
	}
	return render(request,"agendar.html",context)
