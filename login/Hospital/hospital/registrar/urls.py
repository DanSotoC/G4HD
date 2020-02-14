from django.conf.urls import url
from registrar import views

urlpatterns =[

url(r'formulario/(?P<id>\d+)$',views.formulario,name="formulario"),

]