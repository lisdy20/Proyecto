from django.contrib import admin
from entradamigrante.models import Entradamigrante

# Register your models here.

class EntradaMigranteAdmin(admin.ModelAdmin):
    list_display = ['migrante', 'fechaentrada', 'módulo']
    list_filter = ['módulo']
    search_fields = ['migrante']

admin.site.register(Entradamigrante, EntradaMigranteAdmin)