from django.contrib import admin
#from django.db import models
from tipodonacion.models import Tipodonacion


# Register your models here.

class TipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'donacion']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Tipodonacion, TipoAdmin)