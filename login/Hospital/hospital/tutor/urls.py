from django.conf.urls import url,re_path
from django.urls import path, include
from tutor import views

urlpatterns =[

url(r'home/',views.home_tutor,name="home_t"),
url(r'perfil/',views.ver_perfil,name="perfil_t"),
url(r'biblioteca/',views.biblioteca_tutor,name="biblioteca_t")
]