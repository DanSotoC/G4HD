from django.shortcuts import render, get_object_or_404
from .models import Usuario, DateReserva
from .models import DateReserva
from .forms import AgendarForm
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .serializers import RutaDataSerializer
from rest_framework import generics

def agendar_usuario(request, id=None):
	form = AgendarForm(request.POST or None)
	queryset = get_object_or_404(Usuario, idDatosPer=id)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("agendar_all")
	context = {

		"form": form,
		"object_list": queryset,
		"num": queryset.Rut,
	}
	return render(request,"agendar.html",context)


class CreateView(generics.RetrieveUpdateDestroyAPIView):
	queryset = DateReserva.objects.all()
	serializer_class = RutaDataSerializer
	lookup_field = 'Rut'

	def perform_create(self, serializer, *args, **kwargs):
		serializer.save()

