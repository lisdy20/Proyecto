# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from entradamigrante.models import Entradamigrante
from migrante.models import Migrante
from ruta.models import Ruta

# Create your models here.

class Salidamigrante(models.Model):
    idsalida = models.AutoField(db_column='IdSalida', primary_key=True) 
    migrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FKIdMigrante')  
    fechasalida = models.DateTimeField('Fecha de Salida', db_column='FechaSalida')  
    ruta = models.ForeignKey(Ruta, models.DO_NOTHING, db_column='FkIdRuta') 

    def __str__(self):
        return '%s %s' % (self.migrante, self.ruta)

    
    def save(self, *args, **kwargs):
        """
           Obtenemos la ultima entrada del migrante sobreescribimos un valor a
           True para valer que esta entrada ya no cuenta debido que el migrante
           ya hizo su salida.
           Vease la funcion en modelo de Modulo -> def disponibilidad
        """
        entrada = Entradamigrante.objects.filter(migrante=self.migrante).last() 
        entrada.checkout = True
        entrada.save()
        super(Salidamigrante, self).save(*args, **kwargs)
        pass


    class Meta:
        verbose_name = 'Salida de Migrante'
        verbose_name_plural = 'Salidas de Migrante'

    def pdf_comprobante(self):
        return mark_safe(u'<a href="/ruta-de-riesgo/?id=%s" target="_blank" class="addlink">IMPRIMIR</a>'% self.ruta.pk)