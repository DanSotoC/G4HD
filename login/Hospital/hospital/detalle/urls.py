from django.conf.urls import url,re_path
from django.urls import path, include
from detalle import views

urlpatterns =[

url(r'paciente/(?P<id>\d+)$',views.usuario_detail, name="paciente_detalle"),
url(r'tutor/(?P<id>\d+)$',views.tutor_detail, name="tutor_detalle"),
url(r'personal/(?P<id>\d+)$',views.especialista_detail, name="especialista_detalle"),

]