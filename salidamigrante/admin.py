from django.contrib import admin
from salidamigrante.models import Salidamigrante

# Register your models here.

class SalidaAdmin(admin.ModelAdmin):
    list_display = ['migrante', 'fechasalida', 'ruta' , 'pdf_comprobante']
    search_fields = ['migrante', 'ruta']

admin.site.register(Salidamigrante, SalidaAdmin)