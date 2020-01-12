from django.conf.urls import url,re_path
from django.urls import path, include
from lista import views

urlpatterns =[

url(r'listpa/',views.usuarios_listpa,name="listpaciente"),
url(r'listen',views.usuarios_listen, name="listenfermero"),

]