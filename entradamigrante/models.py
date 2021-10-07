# -*- coding: utf-8 -*-
from django.db import models
from migrante.models import Migrante

# Create your models here.

class Entradamigrante(models.Model):
    idmovilidad = models.AutoField(db_column='IdMovilidad', primary_key=True) 
    #salida = models.BooleanField("Salida" , default=False)
    migrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FkIdMigrante') 
    fechaentrada = models.DateTimeField('Fecha de Entrada', db_column='FechaEntrada') 
    módulo = models.ForeignKey(
        'modulo.modulo',
        related_name='modulo', 
        db_column='FkIdModulo',
        on_delete= models.DO_NOTHING,
        )
    descripcion = models.CharField('Descripción', db_column='Descripcion', max_length=254, blank=True,
        null=True) 

    def __str__(self):
        return '%s %s' % (self.migrante, self.módulo)

    class Meta:
        verbose_name = 'Entrada Migrante'
        verbose_name_plural = 'Entrada Migrantes'
        managed = False
        db_table = 'entradamigrante'