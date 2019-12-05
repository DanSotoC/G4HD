from django.urls import include, path


urlpatterns = [
    path('accountsa/', include('django.contrib.auth.urls'))
]

