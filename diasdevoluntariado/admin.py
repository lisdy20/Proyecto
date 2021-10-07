from django.contrib import admin
from diasdevoluntariado.models import Diasdevoluntariado

class DiaVoluntriadoAdmin(admin.ModelAdmin):
    list_display = ['diaarealizar', 'horasaprox', 'voluntario']
    search_fields = ['voluntario']
    

admin.site.register(Diasdevoluntariado, DiaVoluntriadoAdmin)