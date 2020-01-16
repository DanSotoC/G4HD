#especialista/urls.py

from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home_especialista, name="home"),
    url(r'^ausencia_paciente/$', views.ausencia_paciente, name="ausencia_paciente"),
    url(r'^ausencia_paciente_detalle/(?P<id>\d+)$', views.ausencia_paciente_detalle, name="ausencia_paciente_detalle"),
    url(r'^ausencia_paciente_form/(?P<id>\d+)$', views.ausencia_paciente_form, name="ausencia_paciente_form"),
    ]