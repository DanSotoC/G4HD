from django.conf.urls import url, re_path
from biblioteca import views
from .views import model_form_upload, biblioteca, model_form_delete,model_form_edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^home/$',views.biblioteca,name='biblioteca'),
url(r'^subir_archivo/$',views.model_form_upload,name='form_archivos'),
url(r'^subir_archivo_unico/(?P<id>\d+)$',views.model_form_upload_unico,name='form_archivos_unico'),
url(r'^eliminar/(?P<id>\d+)$',views.model_form_delete, name="form_archivos_delete"),
url(r'^editar/(?P<id>\d+)$',views.model_form_edit, name="form_archivos_edit"),
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)