from django.contrib import admin

# Register your models here.
from .models import Usuario



class UsuarioModelAdmin(admin.ModelAdmin):
	list_display = ["Rut","Telefono", "updated", "timestamp"]
	list_display_links = ["Rut", "updated", "timestamp"]
	list_filter = ["timestamp", "updated"]
	search_fields = ["Primer_Nombre","Primer_Apellido", "Segundo_Apellido","Rut"]
	#search fields: agregar busqueda por tipo de usuario (paciente, tutor, doctor)

	class Meta:
		model = Usuario

admin.site.register(Usuario,UsuarioModelAdmin)