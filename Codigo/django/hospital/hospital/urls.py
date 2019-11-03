"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from login import urls as l_urls
from especialista import  urls as e_urls
from django.conf import settings
from django.conf.urls.static import static
from biblioteca import urls as b_urls
from equipo import urls as eq_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/', include(l_urls)),
    url(r'^especialista/', include(e_urls)),
    path(r'biblioteca/', include(b_urls)),
    url(r'^equipo/', include(eq_urls)),




]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
