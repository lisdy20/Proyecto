# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Pais(models.Model):
    idpais = models.AutoField(db_column='IdPais', primary_key=True)  
    nombre = models.CharField('País', db_column='Nombre', max_length=50) 

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        managed = False
        db_table = 'pais'