from django.contrib import admin
#from django.db import models
from tipodonacion.models import Tipodonacion


# Register your models here.

class TipoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'item', 'cantidad', 'donacion']
    list_filter = ['tipo']
    search_fields = ['tipo', 'item']

admin.site.register(Tipodonacion, TipoAdmin)