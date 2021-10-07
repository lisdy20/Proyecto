# -*- coding: utf-8 -*-
from django.db import models
from donacion.models import Donacion

# Create your models here.

class Tipodonacion(models.Model):
    idtipodonacion = models.AutoField(db_column='IdTipoDonacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField('Tipo', db_column='Nombre', max_length=75)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    donacion = models.ForeignKey(Donacion, models.DO_NOTHING, db_column='FkIdDonacion')
    
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.donacion)

    class Meta:
        verbose_name = 'Tipo de Donación'
        verbose_name_plural = 'Tipo de Donaciones'
        managed = False
        db_table = 'tipodonacion'