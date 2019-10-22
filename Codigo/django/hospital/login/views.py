from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import views

def usuarios_home(request):
	return HttpResponse("<h1>Holaaaa</h1>")