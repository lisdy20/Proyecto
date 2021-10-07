# -*- coding: utf-8 -*-
from django.db import models
from migrante.models import Migrante
from entradamigrante.models import Entradamigrante

# Create your models here.

class Modulo(models.Model):
    idmodulo = models.AutoField(db_column='IdModulo', primary_key=True) 
    nombre = models.CharField('Módulo', db_column='Nombre', max_length=50)  
    capacidad = models.IntegerField('Capacidad', db_column='Capacidad') 

    def __str__(self):
        return '%s' % (self.nombre)

    def disponibilidad(self):
        migrantes = Entradamigrante.objects.filter(módulo_id=self.pk)
        diponible = self.capacidad - migrantes.count()
        return diponible

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'