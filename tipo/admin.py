from django.contrib import admin
from tipo.models import Tipo

# Register your models here.

class TipoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Tipo, TipoAdmin)