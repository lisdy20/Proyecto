# -*- coding: utf-8 -*-
from django.db import models
from donacion.models import Donacion
from tipo.models import Tipo

# Create your models here.

class Tipodonacion(models.Model):
    idtipodonacion = models.AutoField(db_column='IdTipoDonacion', primary_key=True) 
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='FkIdTipo')
    item = models.CharField('Artículo/Item', db_column='Item', max_length=100)
    cantidad = models.IntegerField(db_column='Cantidad')  
    donacion = models.ForeignKey(Donacion, models.DO_NOTHING, db_column='FkIdDonacion')
    
    
    def __str__(self):
        return '%s %s' % (self.tipo, self.donacion)

    class Meta:
        verbose_name = 'Detalle de Donación'
        verbose_name_plural = 'Detalle de Donaciones'