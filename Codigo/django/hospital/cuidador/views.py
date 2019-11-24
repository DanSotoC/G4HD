from django.shortcuts import render, redirect, render_to_response
from biblioteca.models import Archivo
from django.views.generic import TemplateView ,View
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def home_cuidador(request):
	return render(request,"home_cuidador.html")

def biblioteca_cuidador(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_cuidador.html',{'archivo':archivo})