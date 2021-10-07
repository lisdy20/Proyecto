# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Creencias(models.Model):
    idcreencia = models.AutoField(db_column='IdCreencia', primary_key=True)  
    nombre = models.CharField('Creencia Religiosa:', db_column='Nombre', max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'Creencia Religiosa'
        verbose_name_plural = 'Creencias Religiosas'