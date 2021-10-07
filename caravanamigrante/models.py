# -*- coding: utf-8 -*-
from django.db import models
from pais.models import Pais
from origencaravana.models import Origencaravana

# Create your models here.

class Caravanamigrante(models.Model):
    idcaravana = models.AutoField(db_column='IdCaravana', primary_key=True) 
    nombre = models.CharField('Nombre de Caravana', db_column='Nombre', max_length=50) 
    país = models.ForeignKey(Pais, models.DO_NOTHING, db_column='FkIdPais')  
    origen = models.ForeignKey(Origencaravana, models.DO_NOTHING, db_column='FkOrigen') 


    def __str__(self):
        return '%s %s' % (self.nombre, self.país)
        
    class Meta:
        verbose_name = 'Caravana Migrante'
        verbose_name_plural = 'Caravana Migrantes'
        managed = False
        db_table = 'caravanamigrante'

    
