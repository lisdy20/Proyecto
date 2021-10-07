from django.contrib import admin
from donacion.models import Donacion
from tipodonacion.models import Tipodonacion

# Register your models here.

class TipoDonacionTabular(admin.TabularInline):
	model = Tipodonacion
	extra = 0
	min_num = 1
	max_num = 15

class DonacionAdmin(admin.ModelAdmin):
    inlines= [TipoDonacionTabular,]
    list_display = ['nombre', 'telefono', 'direccion', 'descripcion', 'fechadeentrega', 'usuario']
    search_fields = ['nombre']

admin.site.register(Donacion, DonacionAdmin)