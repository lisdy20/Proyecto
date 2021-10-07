from django.contrib import admin
from ruta.models import Ruta

# Register your models here.

class RutaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'destino']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Ruta, RutaAdmin)