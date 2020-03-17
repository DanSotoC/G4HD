"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from biblioteca import urls as biblio_urls
from dashboard import urls as dash_urls
from tutor import urls as tutor_urls
from detalle import urls as det_urls
from django.conf import settings
from django.conf.urls.static import static
from especialista import urls as especialista_urls
from equipos import urls as equipos_urls
from redireccion import urls as red
from visita import urls as agnd_visita
from registrar import urls as abc


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path(r'',include('Home.urls')),
    path(r'administrador/',include('lista.urls')),
    path(r'admbiblio/',include(biblio_urls)),
    path(r'dashboard/',include(dash_urls)),
    path(r'tutor/',include(tutor_urls)),
    path(r'detalle/',include(det_urls)),
    path(r'especialista/',include(especialista_urls)),
    path(r'equipos/',include(equipos_urls)),
    path(r'red/',include(red)),
    path(r'visita/',include(agnd_visita)),
    path(r'abc/',include(abc)),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
