from django.contrib import admin
from creencias.models import Creencias

# Register your models here.

class CreenciasAdmin(admin.ModelAdmin):
    list_filter = ['nombre']

admin.site.register(Creencias, CreenciasAdmin)