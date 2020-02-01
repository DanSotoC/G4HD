#especialista/urls.py

from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home_especialista, name="home_e"),
    url(r'^perfil/$', views.ver_perfil_e, name="perfil_e"),
    url(r'^biblioteca/$', views.biblioteca_e, name="biblioteca_e"),
    
    ]