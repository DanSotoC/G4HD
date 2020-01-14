from django.shortcuts import render
from biblioteca.models import Archivo
from django.views.generic import TemplateView ,View
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def home_tutor(request):
	return render(request,"home_tutor.html")

def biblioteca_tutor(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_tutor.html',{'archivo':archivo})
