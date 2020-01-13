from django.conf.urls import url,re_path
from django.urls import path, include
from dashboard import views

urlpatterns =[

url(r'home/',views.home,name="dash"),

]