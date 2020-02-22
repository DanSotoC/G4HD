from django.shortcuts import render, redirect, get_object_or_404
from .models import Archivo, Archivo_Unico
from usuarios.models import Paciente
from django.views.generic import TemplateView ,View
from .forms import DocumentForm, DocumentFormUnico
from django.contrib import messages 
from django.urls import reverse
from django.http import HttpResponseRedirect
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


def biblioteca(request):
	archivo = Archivo.objects.all()
	return render(request,'biblioteca.html',{'archivo':archivo})


def biblioteca_unica(request,id=None):
    px=get_object_or_404(Paciente, id_tutor_id = id) 
    archivo = Archivo_Unico.objects.all()
    context={
        "px":px.id,
        "archivo":archivo,
    }
    return render(request,'biblioteca_unica.html',context)


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


def model_form_upload_unico(request,id=None):
    if request.method == 'POST':
        form = DocumentFormUnico(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(biblioteca)
    else:
        form = DocumentFormUnico()
    return render(request, 'form_archivos_unico.html', {
        'form': form,'id':id
    })



def model_form_delete(request,id):
    
    archivo=Archivo.objects.get(id=id)
    if request.method=='POST':
        os.remove(str(archivo.file))
        archivo.delete()
        return redirect(biblioteca)
    return render(request,'form_archivos_delete.html', {'archivo':archivo})

def model_form_delete_unico(request,id):
    
    archivo=Archivo_Unico.objects.get(id=id)
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




