from django.shortcuts import render, redirect
from .models import Archivo
from django.views.generic import TemplateView ,View
from .forms import DocumentForm

from django.contrib import messages 
from django.urls import reverse
from django.http import HttpResponseRedirect
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


def biblioteca(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca.html',{'archivo':archivo})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(biblioteca)
    else:
        form = DocumentForm()
    return render(request, 'form_archivos.html', {
        'form': form
    })


def model_form_delete(request,id):
    
    archivo=Archivo.objects.get(id=id)
    if request.method=='POST':
        os.remove(str(archivo.file))
        archivo.delete()
        return redirect(biblioteca)
    return render(request,'form_archivos_delete.html', {'archivo':archivo})



def model_form_edit(request,id):
    archivo=Archivo.objects.get(id=id)
    if request.method=='GET':
        form=DocumentForm(instance=archivo)
    else:
        form=DocumentForm(request.POST,instance=archivo)
        if form.is_valid():
            form.save()
        return redirect(biblioteca)
    return render(request,'form_archivos.html',{'form':form})