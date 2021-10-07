# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Origencaravana(models.Model):
    idcaravana = models.AutoField(db_column='IdCaravana', primary_key=True)  
    lugar = models.CharField(db_column='Lugar', max_length=60)  

    def __str__(self):
        return '%s' % (self.lugar)

    class Meta:
        verbose_name = 'Origen Caravana'
        verbose_name_plural = 'Origen Caravanas'