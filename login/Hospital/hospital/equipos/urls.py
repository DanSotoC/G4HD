
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^crear-equipo/$', views.Crear_equipo_view, name="crear-equipo"),
 url(r'^listar-equipo/$', views.Listar_equipo_view, name="listar-equipo"),
 url(r'^asignar-equipo/$', views.Asignar_equipo_view, name="asignar-equipo"),


]