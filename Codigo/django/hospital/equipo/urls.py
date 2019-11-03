from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^crear/', views.crear_equipo , name='crear_equipo'),
     url(r'^registrar/', views.registrar_funcionario , name='registrar_funcionario'),
]

