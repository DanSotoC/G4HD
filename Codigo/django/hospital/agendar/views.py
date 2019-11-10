from django.shortcuts import render, get_object_or_404
from .models import Usuario, DateReserva
from .models import DateReserva
from .forms import AgendarForm
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from .serializers import RutaDataSerializer
from rest_framework import generics
from geopy.geocoders import Nominatim

def agendar_usuario(request, id=None):
	form = AgendarForm(request.POST or None)
	queryset = get_object_or_404(Usuario, idDatosPer=id)
	Dir = queryset.Domicilio+" Santiago, "+queryset.Comuna
	nom = Nominatim()
	n=nom.geocode(Dir)

	"""lat = n.latitude
	lon = n.longitude"""

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("agendar_all")
	context = {

		"form": form,
		"object_list": queryset,
		"num": queryset.Rut,
		"dir": Dir,
		"la":n.latitude,
		"lo":n.longitude,
		
	}
	return render(request,"agendar.html",context)


class CreateView(generics.RetrieveUpdateDestroyAPIView):
	queryset = DateReserva.objects.all()
	serializer_class = RutaDataSerializer
	lookup_field = 'Rut'

	def perform_create(self, serializer, *args, **kwargs):
		serializer.save()

