# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Ruta(models.Model):
    idruta = models.AutoField(db_column='IdRuta', primary_key=True)  
    nombre = models.CharField('Nombre de la Ruta', db_column='Nombre', max_length=50)  
    destino = models.CharField(db_column='Destino', max_length=50)  

    def __str__(self):
        return '%s %s' % (self.nombre, self.destino)

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'