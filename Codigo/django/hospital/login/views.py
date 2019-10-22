from django.shortcuts import render
from django.shortcuts import HttpResponse


def usuarios_create(request):
	return HttpResponse("<h1>Create</h1>")

def usuarios_detail(request):
	return HttpResponse("<h1>Detail</h1>")

def usuarios_list(request):
	
	context = {
		"title": "My User List"
	}
	#example of context form
	return render(request,"index.html",context)

def usuarios_update(request):
	return HttpResponse("<h1>Update</h1>")

def usuarios_delete(request):
	return HttpResponse("<h1>Delete</h1>")

