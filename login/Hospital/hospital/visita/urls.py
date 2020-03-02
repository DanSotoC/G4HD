from django.conf.urls import url,re_path
from django.urls import path, include
from visita import views

urlpatterns =[

url(r'hora/(?P<id>\d+)$',views.agendar_visita, name="agendar_visita"),
url(r'lista/',views.agendar_lista, name="agendar_lista"),
url(r'paciente/',views.visita_paciente, name="visita_paciente"),
url(r'all/(?P<id>\d+)$',views.visita_paciente_admin, name="visita_paciente_admin"),
url(r'^(?P<id>\d+)/borrar/$', views.borrar_fecha,name="borrar_fecha"),
url(r'^(?P<id>\d+)/delete/$', views.borrar_lista,name="delete_lista"),
url(r'^(?P<id>\d+)/edit/$', views.visita_update, name="update_fecha"),
url(r'reagendar/',views.reagendar, name="reagendar"),
url(r'detalle/(?P<id>\d+)$',views.visita_paciente_detalle, name="visita_paciente_detalle"),
url(r'hoy/',views.agendar_lista_hoy, name="agendar_lista_hoy"),
url(r'asignarequipo/(?P<id>\d+)$',views.asignar_equipo_visita, name="asignar_equipo_visita"),

]