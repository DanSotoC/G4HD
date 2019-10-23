from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Usuario
from .forms import UsuarioForm


def usuarios_create(request):
	form = UsuarioForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

	context = {

		"form": form,
	}
	return render(request,"create_form.html",context)

def usuarios_detail(request, id=None):
	instance = get_object_or_404(Usuario, idDatosPer=id)
	context = {
		"nom": instance.Primer_Nombre,
		"pap": instance.Primer_Apellido,
		"sap": instance.Segundo_Apellido,
		"instance": instance,
	}
	#example of context form
	return render(request,"details.html",context)

def usuarios_list(request):
	queryset = Usuario.objects.all()
	context = {
		"object_list": queryset,
	}
	#example of context form
	return render(request,"index.html",context)

def usuarios_update(request):
	return HttpResponse("<h1>Update</h1>")

def usuarios_delete(request):
	return HttpResponse("<h1>Delete</h1>")

