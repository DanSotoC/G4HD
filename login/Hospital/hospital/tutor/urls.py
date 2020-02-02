from django.conf.urls import url,re_path
from django.urls import path, include
from tutor import views

urlpatterns =[

url(r'home/',views.home_tutor,name="home_t"),
url(r'perfil/',views.ver_perfil,name="perfil_t"),
url(r'biblioteca/',views.biblioteca_tutor,name="biblioteca_t"),
url(r'tutor/edit/(?P<perfil>\d+)/(?P<id_detalle>\d+)$',views.Tutor_edit, name="Tutor_edit"),
url(r'paciente/edit/(?P<id_tutor>\d+)/(?P<id_paciente>\d+)$',views.Paciente_edit, name="Paciente_edit"),
]