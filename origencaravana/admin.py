from django.contrib import admin
from origencaravana.models import Origencaravana

# Register your models here.

class OrigenAdmin(admin.ModelAdmin):
    list_display = ['lugar']
    list_filter = ['lugar']
    search_fields = ['lugar']

admin.site.register(Origencaravana, OrigenAdmin)