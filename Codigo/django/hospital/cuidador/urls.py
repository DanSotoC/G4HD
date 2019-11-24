from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/', views.home_cuidador , name='home_cuidador'),
    url(r'^biblioteca/', views.biblioteca_cuidador , name='cuidador_biblioteca'),
]

