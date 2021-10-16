from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Entidad(models.Model):
    identidad = models.AutoField(db_column='IdEntidad', primary_key=True)
    nombre = models.CharField('Nombre o Entidad', db_column='Nombre', max_length=200)


    def __str__(self):
        return '%s' % (self.nombre)


    def donaciones_del_mes(self):
        return mark_safe(u'<a href="/donaciones-mensuales/?id=%s" target="_blank" class="addlink">Donacion mensual</a>'% self.pk)

    def historial_de_donaciones(self):
        return mark_safe(u'<a href="/historial-de-donaciones/?id=%s" target="_blank" class="addlink">Historial de donaciones</a>'% self.pk)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'