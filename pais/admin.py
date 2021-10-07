from django.contrib import admin
from pais.models import Pais

# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Pais, PaisAdmin)