from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/agendar/$', views.agendar_usuario , name='agendar'),

]

