from django.contrib import admin
from modulo.models import Modulo
# Register your models here.

class ModuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad' , 'disponibilidad']
    search_fields = ['nombre']

admin.site.register(Modulo, ModuloAdmin)