from django.contrib import admin
from entidad.models import Entidad

# Register your models here.
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['nombre' , 'donaciones_del_mes','historial_de_donaciones']
    search_fields = ['nombre']

admin.site.register(Entidad, EntidadAdmin)