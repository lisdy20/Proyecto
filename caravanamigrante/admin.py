from django.contrib import admin
from caravanamigrante.models import Caravanamigrante
from migrante.models import Migrante


# Register your models here.


class MigranteTabular(admin.TabularInline):
	model = Migrante
	extra = 0
	min_num = 1
	max_num = 15

class CaravanamigranteAdmin(admin.ModelAdmin):
    inlines= [MigranteTabular,]
    list_display = ['nombre', 'país', 'origen']
    list_filter = ['país']
    search_fields = ['nombre', 'país']
    

admin.site.register(Caravanamigrante, CaravanamigranteAdmin)