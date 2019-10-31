
from django.shortcuts import render
from django.views.generic import TemplateView


def home_especialista(request):
	return render(request,"index_especialista.html")

def ausencia_paciente(request):
	return render(request,"ausencia_paciente.html")