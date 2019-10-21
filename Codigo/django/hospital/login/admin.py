from django.contrib import admin

# Register your models here.
from .models import Usuario



class UsuarioModelAdmin(admin.ModelAdmin):
	list_display = ["Rut"]
	list_display_links = ["Rut"]
	list_filter = ["Rut", "Primer_Nombre"]
	search_fields = ["Primer_Nombre","Primer_Apellido","Rut"]

	class Meta:
		model = Usuario

admin.site.register(Usuario,UsuarioModelAdmin)