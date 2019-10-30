
from django.shortcuts import render
from django.views.generic import TemplateView


def home_especialista(request):
	return render(request,"index_especialista.html")