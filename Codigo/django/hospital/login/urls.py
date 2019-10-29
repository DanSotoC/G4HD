"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from login import views
from . import views

urlpatterns = [
    url(r'^create/$', views.usuarios_create),
    url(r'^(?P<id>\d+)/$', views.usuarios_detail, name='detail'),
    url(r'^listen/$', views.usuarios_listen, name='listen'),
    url(r'^listpa/$', views.usuarios_listpa, name='listpa'),
    url(r'^(?P<id>\d+)/edit/$', views.usuarios_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.usuarios_delete),
    url(r'^home/$', views.home, name="home"),
    url(r'^asignar/$', views.asignar, name="asignar"),
    url(r'^agendar/$', views.agendar, name="agendar"),
    url(r'^formar/$', views.formar, name="formar"),
]
