from django.contrib import admin
from entradamigrante.models import Entradamigrante
from migrante.models import Migrante
from salidamigrante.models import Salidamigrante

# Register your models here.

class SalidaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
            This functions used for filter migrantes in selection list
            in admin form.
        """
        ids = []
        migrantes = Entradamigrante.objects.filter(checkout=False)
        for m in migrantes:
            ids.append(m.migrante.pk)
        if db_field.name == "migrante":
            kwargs["queryset"] = Migrante.objects.filter(pk__in=ids)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ['migrante', 'fechasalida', 'ruta' , 'pdf_comprobante']
    search_fields = ['migrante', 'ruta']

admin.site.register(Salidamigrante, SalidaAdmin)