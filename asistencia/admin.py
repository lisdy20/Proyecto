from django.contrib import admin
from asistencia.models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['voluntario', 'entrada', 'salida', 'creado']
    search_fields = ['voluntario']

admin.site.register(Asistencia, AsistenciaAdmin)
