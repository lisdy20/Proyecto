from django.contrib import admin
from entidad.models import Entidad

# Register your models here.
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

admin.site.register(Entidad, EntidadAdmin)