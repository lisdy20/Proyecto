from django.contrib import admin
from caravanamigrante.models import Caravanamigrante
from migrante.models import Migrante


# Register your models here.


class MigranteTabular(admin.TabularInline):
	model = Migrante
	extra = 1

class CaravanamigranteAdmin(admin.ModelAdmin):
    inlines= [MigranteTabular]
    search_fields = ['nombre' , 'país']
    list_display = ['nombre', 'país', 'origen']
    ordering = ['nombre']
    #autocomplete_fields = ['caravanamigrante']

    list_filter = ['país']
    search_fields = ['nombre', 'país']
    
    

admin.site.register(Caravanamigrante, CaravanamigranteAdmin)