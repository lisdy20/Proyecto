from django.contrib import admin
from caravanamigrante.models import Caravanamigrante
from migrante.models import Migrante
# Register your models here.

class MigranteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido', 'telefono', 'genero', 'edad', 'fechanacimiento', 'nacionalidad', 'usuario']
    list_filter = ['genero', 'nacionalidad']
    search_fields = ['nombre','apellido']

admin.site.register(Migrante, MigranteAdmin)