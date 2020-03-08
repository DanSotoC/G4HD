from django.conf.urls import url
from registrar import views

urlpatterns =[

url(r'formulario/(?P<id>\d+)$',views.formulario,name="formulario"),
url(r'formularioverdetalle/(?P<id>\d+)$',views.ver_formulario,name="ver_formulario_detalle"),
url(r'reg/(?P<id>\d+)$',views.ver_registro_admin,name="ver_registro_adm"),
]